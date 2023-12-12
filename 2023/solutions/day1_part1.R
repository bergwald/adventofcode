# Advent of Code - Day 1 - Part 1

solution <- function(lines) {
  sum <- 0
  for (line in lines) {
    chars <- unlist(strsplit(line, ""))
    digits <- chars[
      chars %in% c("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    ]
    number <- as.numeric(paste0(digits[1], digits[length(digits)]))
    sum <- sum + number
  }
  return(sum)
}

# Example input
example <- "1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"
print(solution(strsplit(example, "\n")[[1]]))

# Actual input
file_path <- "2023/inputs/input1.txt"
lines <- readLines(file_path)
print(solution(lines))
