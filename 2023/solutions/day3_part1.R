# Advent of Code - Day 3 - Part 1

solution <- function(input) {
  board <- input
  board <- Reduce(rbind, strsplit(board, ""))
  board <- cbind(".", rbind(".", board, "."), ".")
  sum <- 0
  row_idx <- 1
  for (row in input) {
    matches <- gregexpr("\\d+", row)
    numbers <- regmatches(row, matches)[[1]]
    for (i in seq_along(numbers)) {
      num <- numbers[i]
      start_pos <- matches[[1]][i]
      end_pos <- start_pos + nchar(num) - 1
      adjacent <- FALSE
      for (r in row_idx:(row_idx+2)) {
        for (c in start_pos:(end_pos+2)) {
          if (!grepl("^[\\.0-9]$", board[r, c])) {
            adjacent <- TRUE
          }
        }
      }
      if (adjacent) {
        sum <- sum + as.numeric(num)
      }
    }
    row_idx <- row_idx + 1
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
