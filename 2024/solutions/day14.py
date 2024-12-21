import math
from contextlib import redirect_stdout
from util_funcs import file_to_list

def display_grid(robots, width, height):
    grid = [[0] * width for _ in range(height)]
    for robot in robots:
        if robot["p_x"] < width and robot["p_y"] < height:
            grid[robot["p_y"]][robot["p_x"]] += 1
        else:
            print(f"Error: {robot}")
    for line in grid:
        print("".join(["." if x == 0 else str(x) for x in line]))
    print("\n")

def part1(robot_info, width, height, seconds):
    # Parse input
    robots = []
    for line in robot_info:
        position, velocity = line.split(" ")
        p_x, p_y = position[2:].split(",")
        v_x, v_y = velocity[2:].split(",")
        robots.append({"p_x" : int(p_x), "p_y": int(p_y), "v_x": int(v_x), "v_y": int(v_y)})
    # Simulate the movement of the robots
    # display_grid(robots, width, height)
    for _ in range(seconds):
        for i, robot in enumerate(robots):
            new_p_x = robot["p_x"] + robot["v_x"]
            new_p_y = robot["p_y"] + robot["v_y"]
            if new_p_x >= width: new_p_x -= width
            if new_p_y >= height: new_p_y -= height
            if new_p_x < 0: new_p_x += width
            if new_p_y < 0: new_p_y += height
            robot["p_x"] = new_p_x
            robot["p_y"] = new_p_y
            robots[i] = robot
    # Calculate the number of robots in each quadrant
    # and the product thereof
    vertical_line = (width // 2)
    horizontal_line = (height // 2)
    q1, q2, q3, q4 = 0, 0, 0, 0
    for robot in robots:
        if robot["p_x"] < vertical_line and robot["p_y"] < horizontal_line:
            q1 += 1
        if robot["p_x"] > vertical_line and robot["p_y"] < horizontal_line:
            q2 += 1
        if robot["p_x"] > vertical_line and robot["p_y"] > horizontal_line:
            q3 += 1
        if robot["p_x"] < vertical_line and robot["p_y"] > horizontal_line:
            q4 += 1       
    safety_factor = math.prod(x for x in [q1, q2, q3, q4] if x != 0)
    return safety_factor

def is_christmas_tree(grid):
    for row in grid:
        for element in row:
            if element not in (0, 1):
                return False
    return True

def part2(robot_info, width, height, seconds):
    # Parse input
    robots = []
    for line in robot_info:
        position, velocity = line.split(" ")
        p_x, p_y = position[2:].split(",")
        v_x, v_y = velocity[2:].split(",")
        robots.append({"p_x" : int(p_x), "p_y": int(p_y), "v_x": int(v_x), "v_y": int(v_y)})
    # Simulate the movement of the robots
    # display_grid(robots, width, height)
    for second in range(seconds):
        for i, robot in enumerate(robots):
            new_p_x = robot["p_x"] + robot["v_x"]
            new_p_y = robot["p_y"] + robot["v_y"]
            if new_p_x >= width: new_p_x -= width
            if new_p_y >= height: new_p_y -= height
            if new_p_x < 0: new_p_x += width
            if new_p_y < 0: new_p_y += height
            robot["p_x"] = new_p_x
            robot["p_y"] = new_p_y
            robots[i] = robot
        # Calculate the number of robots in each quadrant
        grid = [[0] * width for _ in range(height)]
        for robot in robots:
            if robot["p_x"] < width and robot["p_y"] < height:
                grid[robot["p_y"]][robot["p_x"]] += 1
        if is_christmas_tree(grid):
            with open("out.txt", "w") as f:
                with redirect_stdout(f):
                    print(second + 1)
                    display_grid(robots, width, height)  
            break
    return second + 1

robot_positions_example = [
    "p=0,4 v=3,-3",
    "p=6,3 v=-1,-3",
    "p=10,3 v=-1,2",
    "p=2,0 v=2,-1",
    "p=0,0 v=1,3",
    "p=3,0 v=-2,-2",
    "p=7,6 v=-1,-3",
    "p=3,0 v=-1,-2",
    "p=9,3 v=2,3",
    "p=7,3 v=-1,2",
    "p=2,4 v=2,-3",
    "p=9,5 v=-3,-3"
]

print(part1(robot_positions_example, width=11, height=7, seconds=100))

robot_positions = file_to_list("2024/inputs/input14.txt")

print(part1(robot_positions, width=101, height=103, seconds=100))

print(part2(robot_positions, width=101, height=103, seconds=10000))
