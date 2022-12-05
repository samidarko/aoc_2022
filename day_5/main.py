import re
from typing import List

instruction_regex = re.compile(
    r"move (?P<quantity>\d+) from (?P<from_stack>\d+) to (?P<to_stack>\d+)")

Supplies = List[List[str]]


def get_top_crates(supplies: Supplies) -> str:
    return "".join([stack[-1] for stack in supplies])


def get_supplies() -> Supplies:
    lines = list(reversed([line.strip("\n") for line in open("state.txt").readlines()]))
    assert lines
    state = [[] for _ in range(len(lines[0]))]
    for line in lines:
        for index, crate in enumerate(line):
            if crate != " ":
                state[index].append(crate)
    return state


def rearrangement_procedure() -> Supplies:
    supplies = get_supplies()
    lines = [line.strip() for line in open("input.txt").readlines()]

    for line in lines:
        result = instruction_regex.match(line)
        instruction = {k: int(v) for k, v in result.groupdict().items()}
        while instruction["quantity"] > 0:
            supplies[instruction["to_stack"] - 1].append(
                supplies[instruction["from_stack"] - 1].pop())
            instruction["quantity"] -= 1

    return supplies


top_crates = get_top_crates(rearrangement_procedure())
assert top_crates == "QMBMJDFTD"
print(top_crates)


def rearrangement_improved_procedure() -> Supplies:
    """CrateMover 9001"""
    supplies = get_supplies()
    lines = [line.strip() for line in open("input.txt").readlines()]

    for line in lines:
        result = instruction_regex.match(line)
        instruction = {k: int(v) for k, v in result.groupdict().items()}
        # going for a temporary stack is just the faster way to complete part two
        # slice + list.extend would be eventually more performant

        stack = []
        while instruction["quantity"] > 0:
            stack.append(
                supplies[instruction["from_stack"] - 1].pop())
            instruction["quantity"] -= 1

        while stack:
            supplies[instruction["to_stack"] - 1].append(stack.pop())

    return supplies


top_crates = get_top_crates(rearrangement_improved_procedure())
assert top_crates == "NBTVTJNFJ"
print(top_crates)
