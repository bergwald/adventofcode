# Advent of Code - Day 1 - Part 2

solution <- function(lines) {
  sum <- 0
  for (line in lines) {
    # Replace words by digits
    line <- gsub("zero", "zero0zero", line)
    line <- gsub("one", "one1one", line)
    line <- gsub("two", "two2two", line)
    line <- gsub("three", "three3three", line)
    line <- gsub("four", "four4four", line)
    line <- gsub("five", "five5five", line)
    line <- gsub("six", "six6six", line)
    line <- gsub("seven", "seven7seven", line)
    line <- gsub("eight", "eight8eight", line)
    line <- gsub("nine", "nine9nine", line)
    # Same as part 1
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
example <- "two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"
print(solution(strsplit(example, "\n")[[1]]))

# Actual input
file_path <- "2023/inputs/input1.txt"
lines <- readLines(file_path)
print(solution(lines))
