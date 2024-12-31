def day17_part1(program):
    registers, instructions = program.split("\n\n")
    register_a, register_b, register_c = [int(x.split(" ")[2]) for x in registers.split("\n")]
    instructions = [int(x) for x in instructions.split(" ")[1].split(",")]
    pointer = 0
    output = []
    while pointer < len(instructions):
        instruction = instructions[pointer]
        literal_operand = instructions[pointer + 1]
        jumped = False
        match literal_operand:
            case 0 | 1 | 2 | 3: combo_operand = literal_operand
            case 4: combo_operand = register_a
            case 5: combo_operand = register_b
            case 6: combo_operand = register_c
        match instruction:
            case 0: register_a = int(register_a / (2 ** combo_operand))
            case 1: register_b = register_b ^ literal_operand
            case 2: register_b = combo_operand % 8
            case 3:
                if register_a != 0:
                    pointer = literal_operand
                    jumped = True
            case 4: register_b = register_b ^ register_c
            case 5: output.append(combo_operand % 8)
            case 6: register_b = int(register_a / (2 ** combo_operand))
            case 7: register_c = int(register_a / (2 ** combo_operand))
        if not jumped:
            pointer += 2
    output = ",".join([str(x) for x in output])
    return output


test_program_1 = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
""".strip()

print(f"Part 1 example 1: {day17_part1(test_program_1)}")

test_program_2 = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
""".strip()

print(f"Part 1 example 2: {day17_part1(test_program_2)}")

test_program_3 = """
Register A: 10
Register B: 0
Register C: 0

Program: 5,0,5,1,5,4
""".strip()

print(f"Part 1 example 3: {day17_part1(test_program_3)}")

with open("2024/inputs/input17.txt", "r") as f:
    program = f.read()

print(f"Part 1: {day17_part1(program)}")
