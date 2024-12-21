from collections import namedtuple
from util_funcs import file_to_list

Coordinate = namedtuple("Coordinate", "x y")

def move(warehouse, coord, new_coord, direction):
    match warehouse[new_coord.x][new_coord.y]:
        case ".":
            warehouse[new_coord.x][new_coord.y] = warehouse[coord.x][coord.y]
            warehouse[coord.x][coord.y] = "."
        case "O":
            match direction:
                case "<": new_O_coord = Coordinate(new_coord.x, new_coord.y - 1)
                case "^": new_O_coord = Coordinate(new_coord.x - 1, new_coord.y)
                case ">": new_O_coord = Coordinate(new_coord.x, new_coord.y + 1)
                case "v": new_O_coord = Coordinate(new_coord.x + 1, new_coord.y)
            warehouse = move(warehouse, new_coord, new_O_coord, direction)
            if warehouse[new_coord.x][new_coord.y] == ".":
                warehouse[new_coord.x][new_coord.y] = warehouse[coord.x][coord.y]
                warehouse[coord.x][coord.y] = "."
        case "#": pass
    return warehouse

def update_coord_robot(warehouse, coord_robot, new_coord):
    if warehouse[new_coord.x][new_coord.y] == "@":
        return new_coord
    else:
        return coord_robot
    
def print_warehouse(warehouse):
    for line in warehouse:
        print("".join(line))
    print("\n")

def part1(warehouse, movements):
    warehouse = [[value for value in line] for line in warehouse]
    coord_robot = (0, 0)
    for i, line in enumerate(warehouse):
        for j, value in enumerate(line):
            if value == "@":
                coord_robot = Coordinate(i, j)
    for movement in movements:
        if movement == "<":
            new_coord = Coordinate(coord_robot.x, coord_robot.y - 1)
            warehouse = move(warehouse, coord_robot, new_coord, movement)
            coord_robot = update_coord_robot(warehouse, coord_robot, new_coord)
        elif movement == "^":
            new_coord = Coordinate(coord_robot.x - 1, coord_robot.y)
            warehouse = move(warehouse, coord_robot, new_coord, movement)
            coord_robot = update_coord_robot(warehouse, coord_robot, new_coord)
        elif movement == ">":
            new_coord = Coordinate(coord_robot.x, coord_robot.y + 1)
            warehouse = move(warehouse, coord_robot, new_coord, movement)
            coord_robot = update_coord_robot(warehouse, coord_robot, new_coord)
        elif movement == "v":
            new_coord = Coordinate(coord_robot.x + 1, coord_robot.y)
            warehouse = move(warehouse, coord_robot, new_coord, movement)
            coord_robot = update_coord_robot(warehouse, coord_robot, new_coord)
    # print_warehouse(warehouse)
    gps_coords = []
    for i in range(len(warehouse)):
        for j in range(len(warehouse[0])):
            if warehouse[i][j] == "O":
                gps_coords.append(100 * i + j)
    return sum(gps_coords)

example_warehouse_1 = [
    "########",
    "#..O.O.#",
    "##@.O..#",
    "#...O..#",
    "#.#.O..#",
    "#...O..#",
    "#......#",
    "########",
]
example_movements_1 = "<^^>>>vv<v>>v<<"

# print(part1(example_warehouse_1, example_movements_1))

example_warehouse_2 = [
    "##########",
    "#..O..O.O#",
    "#......O.#",
    "#.OO..O.O#",
    "#..O@..O.#",
    "#O#..O...#",
    "#O..O..O.#",
    "#.OO.O.OO#",
    "#....O...#",
    "##########",
]

example_movements_2 = "".join([
    "<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^",
    "vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v",
    "><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<",
    "<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^",
    "^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><",
    "^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^",
    ">^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^",
    "<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>",
    "^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>",
    "v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^",
])

print(part1(example_warehouse_2, example_movements_2))

input_day15 = file_to_list("2024/inputs/input15.txt", sep="\n\n")
warehouse = input_day15[0].split("\n")
movements = "".join(input_day15[1].split("\n"))

print(part1(warehouse, movements))
