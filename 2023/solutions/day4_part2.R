# Advent of Code - Day 4 - Part 2

solution <- function(cards) {
  n <- rep(1, length(cards))
  for (i in seq_along(cards)) {
    card <- trimws(strsplit(cards[i], ":")[[1]][2])
    split_card <- strsplit(card, " \\| ")
    winning <- as.integer(unlist(strsplit(split_card[[1]][1], "\\s+")))
    winning <- sapply(winning, trimws)
    my_card <- as.integer(unlist(strsplit(split_card[[1]][2], "\\s+")))
    my_card <- sapply(my_card, trimws)
    wins <- length(intersect(winning, my_card))
    if (wins > 0) {
      increased_cards <- (i + 1): (i + wins)
      n[increased_cards] <- n[increased_cards] + (1 * n[i])
    }
  }
  return(sum(n))
}

# Example input
example <- "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
example <- strsplit(example, "\n")[[1]]
print(solution(example))

# Real input
file_path <- "2023/inputs/input4.txt"
cards <- readLines(file_path)
print(solution(cards))
