# Advent of Code - Day 6 - Part 1

clean <- function(line) {
  line <- trimws(strsplit(line, ":")[[1]][2])
  line <- as.integer(unlist(strsplit(line[[1]][1], "\\s+")))
  return(line)
}

solution <- function(input) {
  time <- clean(input[[1]])
  dist <- clean(input[[2]])
  n <- c()
  for (i in seq_along(time)) {
    w <- 0
    for (j in 0:time[i]) {
      if ((j * (time[i] - j)) > dist[i]) {
        w <- w + 1
      }
    }
    n <- c(n, w)
  }
  return(prod(n))
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