from functools import cache
from util_funcs import file_to_list

@cache
def break_towel(towel, patterns):
    if towel == "":
        return True
    else:
        possible = False
        for pattern in patterns:
            if towel.startswith(pattern):
                if break_towel(towel.removeprefix(pattern), patterns) is True:
                    possible = True
        return possible

def day19_part1(patterns: str, towels: str):
    patterns = patterns.split(", ")
    towels = towels.split("\n")
    possible = sum([break_towel(towel, tuple(patterns)) for towel in towels])
    return possible

test_patterns, test_towels = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
""".strip().split("\n\n")

print(f"Day 19 part 1 example: {day19_part1(test_patterns, test_towels)}")

patterns, towels = file_to_list("2024/inputs/input19.txt", sep = "\n\n")

print(f"Day 19 part 1: {day19_part1(patterns, towels)}")

# Part 2 ----------------------------------------

@cache
def count(towel, patterns):
    if towel == "":
        return 1
    else:
        possibilities = 0
        for pattern in patterns:
            if towel.startswith(pattern):
                possibilities += count(towel.removeprefix(pattern), patterns)
        return possibilities

def day19_part2(patterns: str, towels: str):
    patterns = patterns.split(", ")
    towels = towels.split("\n")
    possibilities = sum([count(towel, tuple(patterns)) for towel in towels])
    return possibilities

print(f"Day 19 part 2 example: {day19_part2(test_patterns, test_towels)}")

print(f"Day 19 part 2: {day19_part2(patterns, towels)}")
