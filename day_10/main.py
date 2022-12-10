# instructions = [line.strip() for line in open("test_input.txt").readlines()]

def part_one(instructions):
    total_cycles = 0
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
            total_cycles += 1
            cycles -= 1
            if total_cycles in [20, 60, 100, 140, 180, 220]:
                signals_strength.append(total_cycles * register_x)

        register_x += value

    return sum(signals_strength)


def main():
    instructions = [line.strip() for line in open("input.txt").readlines()]
    sum_signal_strength = part_one(instructions)
    assert sum_signal_strength == 10760
    print(sum_signal_strength)


if __name__ == "__main__":
    main()
