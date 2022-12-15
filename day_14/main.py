from typing import List
from math import inf
from collections import namedtuple
from dataclasses import dataclass


@dataclass
class Shape:
    min_x: int
    min_y: int
    max_x: int
    max_y: int


Position = namedtuple("Position", "x y")


def to_position(position: str) -> Position:
    x, y = position.split(",")
    return Position(int(x), int(y))


def get_data() -> (Position, Shape):
    lines = [line.strip() for line in open("input.txt").readlines()]

    rocks = []

    min_x, min_y, max_x, max_y = inf, inf, -inf, -inf

    for line in lines:
        rock = []
        for item in line.split(" -> "):
            position = to_position(item)
            min_x, min_y = min(min_x, position.x), min(min_y, position.y)
            max_x, max_y = max(max_x, position.x), max(max_y, position.y)
            rock.append(position)
        rocks.append(rock)
    print(min_x, min_y, max_x, max_y)
    return rocks, Shape(min_x, min_y, max_x, max_y)


def part_one():
    pass


def part_two():
    pass


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
