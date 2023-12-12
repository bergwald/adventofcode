# Advent of Code - Day 2 - Part 2

solution <- function(games) {
  sum <- 0
  for (game in games) {
    min_red <- 0
    min_green <- 0
    min_blue <- 0
    game <- strsplit(game, ":")[[1]][2]
    draws <- strsplit(game, ";")[[1]]
    for (draw in draws) {
      colors <- strsplit(draw, ",")[[1]]
      for (color in colors) {
        splitted <- strsplit(trimws(color), " ")[[1]]
        count <- as.numeric(splitted[1])
        color <- splitted[2]
        if (color == "red") {
          if (count > min_red) {
            min_red <- count
          }
        } else if (color == "green") {
          if (count > min_green) {
            min_green <- count
          }
        } else if (color == "blue") {
          if (count > min_blue) {
            min_blue <- count
          }
        }
      }
    }
    sum <- sum + (min_red * min_green * min_blue)
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