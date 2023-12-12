# Advent of Code - Day 2 - Part 1

solution <- function(games) {
  sum <- 0
  idx <- 1
  for (game in games) {
    possible <- TRUE
    game <- strsplit(game, ":")[[1]][2]
    draws <- strsplit(game, ";")[[1]]
    for (draw in draws) {
      colors <- strsplit(draw, ",")[[1]]
      for (color in colors) {
        splitted <- strsplit(trimws(color), " ")[[1]]
        count <- as.numeric(splitted[1])
        color <- splitted[2]
        if (color == "red") {
          if (count > 12) {
            possible <- FALSE
          }
        } else if (color == "green") {
          if (count > 13) {
            possible <- FALSE
          }
        } else if (color == "blue") {
          if (count > 14) {
            possible <- FALSE
          }
        }
      }
    }
    if (possible == TRUE) {
      sum <- sum + idx
    }
    idx <- idx + 1
  }
  return(sum)
}

# Example input
example <- "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
print(solution(strsplit(example, "\n")[[1]]))

# Real input
file_path <- "2023/inputs/input2.txt"
lines <- readLines(file_path)
print(solution(lines))
