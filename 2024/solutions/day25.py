def calculate_heights(rows):
    heights = []
    for col_idx in range(5):
        col = "".join([rows[row_idx][col_idx] for row_idx in range(7)])
        height = col.count("#") - 1
        heights.append(height)
    return heights


def part1(schematics: str):
    schematics = schematics.strip().split(sep="\n\n")
    locks = []
    keys = []
    for schematic in schematics:
        rows = schematic.split("\n")
        heights = calculate_heights(rows)
        if rows[0] == "#####":
            locks.append(heights)
        else:
            keys.append(heights)
    fitting_pairs = 0
    for lock in locks:
        for key in keys:
            works = True
            for lock_height, key_height in zip(lock, key):
                if lock_height + key_height > 5:
                    works = False
                    break
            if works:
                fitting_pairs += 1
    return fitting_pairs

test_schematics = """
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""

print(f"Part 1 example: {part1(test_schematics)}")

with open("2024/inputs/input25.txt", "r") as f:
    schematics = f.read()

print(f"Part 1: {part1(schematics)}")