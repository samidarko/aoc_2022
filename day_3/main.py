import string


def main():
    data = [line.strip() for line in open("input.txt").readlines()]
    priorities_sum = get_priorities_sum_part_one(data)
    assert priorities_sum == 7674
    print(priorities_sum)

    priorities_sum = get_priorities_sum_part_two(data)
    assert priorities_sum == 2805
    print(priorities_sum)


def get_priorities_sum_part_one(data: list) -> int:
    priorities_sum = 0

    for line in data:
        middle = len(line) // 2
        compartment_a, compartment_b = line[:middle], line[middle:]
        common_items = set(compartment_a).intersection(set(compartment_b))
        assert len(common_items) == 1
        priorities_sum += string.ascii_letters.index(list(common_items)[0]) + 1

    return priorities_sum


def get_priorities_sum_part_two(data: list) -> int:
    group_size = 3
    priorities_sum = 0

    for offset in range(0, len(data), group_size):
        sack_a, sack_b, sack_c, *_ = data[offset:offset + group_size]
        common_items = set(sack_a).intersection(set(sack_b)).intersection(set(sack_c))
        assert len(common_items) == 1, f"should have only one item but got {common_items}"
        priorities_sum += string.ascii_letters.index(list(common_items)[0]) + 1

    return priorities_sum


if __name__ == "__main__":
    main()
