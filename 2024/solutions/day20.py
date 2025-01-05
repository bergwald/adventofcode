from collections import deque
from util_funcs import file_to_list


def find_path(racetrack):
    # Find the start coordinates
    start = None
    for x in range(len(racetrack)):
        for y in range(len(racetrack[0])):
            if racetrack[x][y] == "S":
                start = (x, y)
    # Find the shortest path to the end
    queue = deque([[start]])
    explored = set([start])
    while queue:
        path = queue.popleft()
        pos = path[-1]
        if racetrack[pos[0]][pos[1]] == "E":
            return path
        adjacent_pos = [
            (pos[0] + 1, pos[1]),
            (pos[0] - 1, pos[1]),
            (pos[0], pos[1] + 1),
            (pos[0], pos[1] - 1)
        ]
        for adjacent in adjacent_pos:
            if (0 <= adjacent[0] < len(racetrack) and
                0 <= adjacent[1] < len(racetrack[0])):
                if racetrack[adjacent[0]][adjacent[1]] != "#":
                    if adjacent not in explored:
                        explored.add(adjacent)
                        new_path = list(path)
                        new_path.append(adjacent)
                        queue.append(new_path)


def day20_part1(racetrack, diff):
    path = find_path(racetrack)
    count_cheats = 0
    for i in range(len(path)-diff):
        point_a = path[i]
        for j in range(i+1, len(path)):
            point_b = path[j]
            # Check that the two points are separated by a Manhattan distance of 2
            if abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1]) == 2:
                manhattan_neighbors = lambda x, y: [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
                coords = set(manhattan_neighbors(point_a[0], point_a[1])).intersection(manhattan_neighbors(point_b[0], point_b[1]))
                for coord in coords:
                    if racetrack[coord[0]][coord[1]] == "#":
                        time_saved = j - i - 2
                        # print(coord, point_a, point_b, i, j, time_saved)
                        if time_saved >= diff:
                            count_cheats += 1
    return count_cheats

racetrack_example = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
""".strip().split("\n")

print(f"Day 20 part 1 example: {day20_part1(racetrack_example, 2)}")

racetrack = file_to_list("2024/inputs/input20.txt")

print(f"Day 20 part 1: {day20_part1(racetrack, 100)}")
