from enum import Enum


# TODO replace tuple by named tuple

def to_tuple(item: str) -> tuple[str, str]:
    a, b, *_ = item.strip().split()
    return a, b


tournament = [to_tuple(item) for item in open("input.txt").readlines()]

WINNING_GAME_SCORE = 6
DRAW_GAME_SCORE = 3


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


shapes = {Shape.ROCK, Shape.PAPER, Shape.SCISSORS}


def get_shape(hand: str) -> Shape:
    match hand.upper():
        case "A" | "X":
            return Shape.ROCK
        case "B" | "Y":
            return Shape.PAPER
        case "C" | "Z":
            return Shape.SCISSORS
        case hand:
            raise Exception(f"unknown hand gest {hand}")


def get_shape_score(shape: Shape) -> int:
    match shape:
        case Shape.ROCK:
            return 1
        case Shape.PAPER:
            return 2
        case Shape.SCISSORS:
            return 3


def get_shapes(turn: tuple[str, str]):
    return get_shape(turn[0]), get_shape(turn[1])


def is_winner(player_one: Shape, player_two: Shape) -> bool:
    """returns True is player_one is winner"""
    assert player_one != player_two
    match (player_one, player_two):
        case (Shape.ROCK, Shape.PAPER):
            return False
        case (Shape.ROCK, Shape.SCISSORS):
            return True
        case (Shape.PAPER, Shape.ROCK):
            return True
        case (Shape.PAPER, Shape.SCISSORS):
            return False
        case (Shape.SCISSORS, Shape.ROCK):
            return False
        case (Shape.SCISSORS, Shape.PAPER):
            return True


def get_score(turn: tuple[str, str]) -> int:
    match get_shapes(turn):
        case (opponent, you) if opponent == you:
            return DRAW_GAME_SCORE + get_shape_score(you)
        case (opponent, you) if is_winner(you, opponent):
            return WINNING_GAME_SCORE + get_shape_score(you)
        case (_, you):
            return get_shape_score(you)


print(sum([get_score(game) for game in tournament]))
assert sum([get_score(game) for game in tournament]) == 13675


def get_predicted_score(turn: tuple) -> int:
    match (get_shape(turn[0]), turn[1]):
        case (opponent, "X"):  # you loose
            for shape in shapes.difference({opponent}):
                if is_winner(opponent, shape):
                    return get_shape_score(shape)
        case (opponent, "Y"):  # draw
            return DRAW_GAME_SCORE + get_shape_score(opponent)
        case (opponent, "Z"):  # you win
            for shape in shapes.difference({opponent}):
                if is_winner(shape, opponent):
                    return WINNING_GAME_SCORE + get_shape_score(shape)


print(sum([get_predicted_score(game) for game in tournament]))
assert sum([get_predicted_score(game) for game in tournament]) == 14184
