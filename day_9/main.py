from math import dist
from collections import namedtuple

Position = namedtuple("Coord", "x y")

DIAGONAL_EUCLIDEAN_DISTANCE = 1.4142135623730951


def move_position(position: Position, move) -> Position:
    match move:
        case "U":
            return Position(position.x, position.y + 1)
        case "R":
            return Position(position.x + 1, position.y)
        case "D":
            return Position(position.x, position.y - 1)
        case "L":
            return Position(position.x - 1, position.y)


def update_tail(head: Position, tail: Position, move: str) -> Position:
    if dist(head, tail) <= DIAGONAL_EUCLIDEAN_DISTANCE:
        return tail

    match move:
        case "U" if tail.x == head.x:
            # up move
            return Position(tail.x, tail.y + 1)
        case "U":
            # up move in diagonal
            return Position(head.x, head.y - 1)
        case "R" if tail.y == head.y:
            # right move
            return Position(tail.x + 1, tail.y)
        case "R":
            # right move in diagonal
            return Position(head.x - 1, head.y)
        case "D" if tail.x == head.x:
            # down move
            return Position(tail.x, tail.y - 1)
        case "D":
            # down move in diagonal
            return Position(head.x, head.y + 1)
        case "L" if tail.y == head.y:
            # left move
            return Position(tail.x - 1, tail.y)
        case "L":
            # left move in diagonal
            return Position(head.x + 1, head.y)


def part_one(instructions) -> int:
    head, tail = Position(0, 0), Position(0, 0)
    tail_visited_position = {tail}

    for instruction in instructions:
        move, _steps = instruction.split()
        steps = int(_steps)
        while steps > 0:
            head = move_position(head, move)
            tail = update_tail(head, tail, move)
            tail_visited_position.add(tail)
            steps -= 1

    return len(tail_visited_position)


def main():
    instructions = [line.strip() for line in open("input.txt").readlines()]
    total_visited_position = part_one(instructions)
    assert total_visited_position == 6284
    print(total_visited_position)


if __name__ == "__main__":
    main()
