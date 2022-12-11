# instructions = [line.strip() for line in open("test_input.txt").readlines()]

def part_one(instructions):
    current_cycle = 0
    register_x = 1
    signals_strength = []

    for instruction in instructions:
        match instruction:
            case "noop":
                value = 0
                cycles = 1
            case _:
                add_x, _value = instruction.split()
                assert add_x == "addx"
                value = int(_value)
                cycles = 2

        while cycles > 0:
            current_cycle += 1
            cycles -= 1
            if current_cycle in [20, 60, 100, 140, 180, 220]:
                signals_strength.append(current_cycle * register_x)

        register_x += value

    return sum(signals_strength)


def part_two(instructions):
    row = 0
    row_width = 40
    crt = ["." for _ in range(240)]
    current_cycle = 0
    register_x = 1

    for instruction in instructions:
        match instruction:
            case "noop":
                value = 0
                cycles = 1
            case _:
                add_x, _value = instruction.split()
                assert add_x == "addx"
                value = int(_value)
                cycles = 2

        while cycles > 0:
            sprite_position = register_x + row * row_width
            if sprite_position - 1 <= current_cycle <= sprite_position + 1:
                crt[current_cycle] = "#"
            current_cycle += 1
            if current_cycle % row_width == 0:
                row += 1
            cycles -= 1

        register_x += value

    for row in range(6):
        offset = row * row_width
        print("".join(crt[offset:offset + row_width]))

    print(f"capital letters FPGPHFGH")


def main():
    instructions = [line.strip() for line in open("input.txt").readlines()]
    sum_signal_strength = part_one(instructions)
    assert sum_signal_strength == 10760
    print(sum_signal_strength)
    part_two(instructions)


if __name__ == "__main__":
    main()
