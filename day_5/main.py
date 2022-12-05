import re
from typing import List

instruction_regex = re.compile(
    r"move (?P<quantity>\d+) from (?P<from_stack>\d+) to (?P<to_stack>\d+)")

State = List[List[str]]


def get_supplies() -> State:
    lines = list(reversed([line.strip("\n") for line in open("state.txt").readlines()]))
    assert lines
    state = [[] for _ in range(len(lines[0]))]
    for line in lines:
        for index, crate in enumerate(line):
            if crate != " ":
                state[index].append(crate)
    return state


def rearrangement_procedure() -> State:
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


final_supplies = rearrangement_procedure()
print("".join([stack[-1] for stack in final_supplies]))
