from collections import deque
from util_funcs import file_to_list


def day18_part1(byte_positions, end_x, end_y):
    mem_space = [["."] * (end_y + 1) for _ in range(end_x + 1)]
    for coords in byte_positions:
        x, y = [int(coord) for coord in coords.split(",")]
        mem_space[y][x] = "#"
    # Print map
    # for row in mem_space:
    #     print("".join(row))
    # Find shortest path from 0,0 to end_x, end_y
    start = (0, 0)
    queue = deque([[start]])
    explored = set([start])
    while queue:
        path = queue.popleft()
        pos = path[-1]
        if pos[0] == end_x and pos[1] == end_y:
            return len(path) - 1
        adjacent_pos = [
            (pos[0] + 1, pos[1]),
            (pos[0] - 1, pos[1]),
            (pos[0], pos[1] + 1),
            (pos[0], pos[1] - 1)
        ]
        for adjacent in adjacent_pos:
            if (0 <= adjacent[0] < len(mem_space) and
                0 <= adjacent[1] < len(mem_space[0])):
                if mem_space[adjacent[0]][adjacent[1]] != "#":
                    if adjacent not in explored:
                        explored.add(adjacent)
                        new_path = list(path)
                        new_path.append(adjacent)
                        queue.append(new_path)
    return "Error"


def day18_part2(byte_positions, start_bytes, end_x, end_y):
    for i in range(start_bytes, len(byte_positions)):
        result = day18_part1(byte_positions[:i], end_x, end_y)
        if result == "Error":
            return byte_positions[i-1]


byte_positions_example = [
    "5,4",
    "4,2",
    "4,5",
    "3,0",
    "2,1",
    "6,3",
    "2,4",
    "1,5",
    "0,6",
    "3,3",
    "2,6",
    "5,1",
    "1,2",
    "5,5",
    "2,5",
    "6,5",
    "1,4",
    "0,4",
    "6,4",
    "1,1",
    "6,1",
    "1,0",
    "0,5",
    "1,6",
    "2,0"
]

print(f"Day 18 part 1 example: {day18_part1(byte_positions_example[:12], 6, 6)}")

byte_positions = file_to_list("2024/inputs/input18.txt")

print(f"Day 18 part 1: {day18_part1(byte_positions[:1024], 70, 70)}")

print(f"Day 18 part 2 example: {day18_part2(byte_positions_example, 12, 6, 6)}")

print(f"Day 18 part 2: {day18_part2(byte_positions, 1024, 70, 70)}")
