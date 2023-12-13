# Advent of Code - Day 3 - Part 2

solution <- function(input) {
  board <- input
  board <- Reduce(rbind, strsplit(board, ""))
  board <- cbind(".", rbind(".", board, "."), ".")
  sum <- 0
  row_idx <- 1
  numbers_dict <- c()
  for (row in input) {
    matches <- gregexpr("\\d+", row)
    numbers <- regmatches(row, matches)[[1]]
    for (i in seq_along(numbers)) {
      num <- numbers[i]
      start_pos <- matches[[1]][i]
      end_pos <- start_pos + nchar(num) - 1
      for (pos in start_pos:end_pos) {
        num <- as.numeric(num)
        numbers_dict[sprintf("%d-%d", (row_idx + 1), (pos + 1))] <- num
      }
    }
    row_idx <- row_idx + 1
  }
  for (i in seq_len(nrow(board))) {
    for (j in seq_len(ncol(board))) {
      if (board[i, j] == "*") {
        numbers <- c()
        for (r in (i - 1):(i + 1)) {
          for (c in (j - 1):(j + 1)) {
            coord <- sprintf("%d-%d", r, c)
            if (coord %in% names(numbers_dict)) {
              value <- numbers_dict[[coord]]
              if (!(value %in% numbers)) {
                numbers <- c(numbers, value)
              }
            }
          }
        }
        if (length(numbers) == 2) {
          sum <- sum + Reduce(`*`, numbers)
        }
      }
    }
  }
  return(sum)
}

# Example input
input <- "467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."
input <- strsplit(input, "\n")[[1]]
print(solution(input))

# Real input
file_path <- "2023/inputs/input3.txt"
lines <- readLines(file_path)
print(solution(lines))