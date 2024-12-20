from util_funcs import file_to_list


def part1(machines):
    total_tokens = 0
    for machine in machines:
        a_x, a_y = [int(x[2:]) for x in machine[0][10:].split(", ")]
        b_x, b_y = [int(x[2:]) for x in machine[1][10:].split(", ")]
        p_x, p_y = [int(x[2:]) for x in machine[2][7:].split(", ")]
        min_tokens = 1e6
        opt_c_a = None
        opt_c_b = None
        for c_a in range(100):
            for c_b in range(100):
                res_x = (c_a * a_x) + (c_b * b_x)
                res_y = (c_a * a_y) + (c_b * b_y)
                if res_x == p_x and res_y == p_y:
                    tokens = 3 * c_a + c_b
                    if tokens < min_tokens:
                        min_tokens = tokens
                        opt_c_a = c_a
                        opt_c_b = c_b
        if opt_c_a is not None:
            total_tokens += tokens
    return total_tokens


def part2(machines):
    total_tokens = 0
    for machine in machines:
        a_x, a_y = [int(x[2:]) for x in machine[0][10:].split(", ")]
        b_x, b_y = [int(x[2:]) for x in machine[1][10:].split(", ")]
        p_x, p_y = [int(x[2:]) + 10000000000000 for x in machine[2][7:].split(", ")]
        c_a = (p_x*b_y - p_y*b_x) / (a_x*b_y - a_y*b_x)
        c_b = (p_y*a_x - p_x*a_y) / (a_x*b_y - a_y*b_x)
        if int(c_a) == c_a and int(c_b) == c_b:
            tokens = int(3 * c_a + c_b)
            total_tokens += tokens
    return total_tokens

test_machines = [
    [
        "Button A: X+94, Y+34",
        "Button B: X+22, Y+67",
        "Prize: X=8400, Y=5400"
    ],
    [
        "Button A: X+26, Y+66",
        "Button B: X+67, Y+21",
        "Prize: X=12748, Y=12176"
    ],
    [
        "Button A: X+17, Y+86",
        "Button B: X+84, Y+37",
        "Prize: X=7870, Y=6450"
    ],
    [
        "Button A: X+69, Y+23",
        "Button B: X+27, Y+71",
        "Prize: X=18641, Y=10279"
    ]
]

print(f"Result example part 1: {part1(test_machines)}")

final_machines = [x.split("\n") for x in file_to_list("2024/inputs/input13.txt", sep="\n\n")]
print(f"Result part 1: {part1(final_machines)}")

print(f"Result part 2: {part2(final_machines)}")

