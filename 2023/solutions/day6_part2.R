# Advent of Code - Day 6 - Part 2

library(bit64)

clean <- function(line) {
  line <- trimws(strsplit(line, ":")[[1]][2])
  line <- as.numeric((gsub(" ", "", line, fixed = TRUE)))
  return(line)
}

solution <- function(input) {
  time <- clean(input[[1]])
  dist <- clean(input[[2]])
  b1 <- floor((time + sqrt((time ^ 2) - 4 * dist)) / 2)
  b2 <- ceiling((time - sqrt((time ^ 2) - 4 * dist)) / 2)
  return(b1 - b2 + 1)
}

# Example input
example <- "Time:      7  15   30
Distance:  9  40  200"
example <- strsplit(example, "\n")[[1]]
print(solution(example))

# Real input
file_path <- "2023/inputs/input6.txt"
input <- readLines(file_path)
print(solution(input))