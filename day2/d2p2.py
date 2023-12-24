import sys
import re
from collections import namedtuple
from dataclasses import dataclass
from typing import Match
from functools import reduce


# Round = namedtuple("Round", ["red", "green", "blue"])


@dataclass
class Round:
    red: int = 0
    green: int = 0
    blue: int = 0

    def __str__(self):
        return f"Round: red: {self.red}, green: {self.green}, blue: {self.blue}"


MaxValues = namedtuple("MaxValues", ["red", "green", "blue"])


class Game:
    rounds: list[Round]
    id: int
    original_input: str

    def __init__(self, id: int, original_input: str) -> None:
        # Instance attribute with type hint
        self.id: int = id
        self.original_input: str = original_input

    def __str__(self):
        return f"Game: {self.id}, Rounds: {self.rounds}"

    def get_max_rgb_values(self) -> MaxValues:
        max_red = max(round.red for round in self.rounds) if self.rounds else 0
        max_green = max(round.green for round in self.rounds) if self.rounds else 0
        max_blue = max(round.blue for round in self.rounds) if self.rounds else 0
        return MaxValues(red=max_red, green=max_green, blue=max_blue)

    def is_possible(self, max_values: MaxValues) -> bool:
        game_maxes: MaxValues = self.get_max_rgb_values()
        return all(
            getattr(game_maxes, color) <= getattr(max_values, color)
            for color in ["red", "green", "blue"]
        )

    def get_power(self) -> int:
        max_values: MaxValues = self.get_max_rgb_values()
        return reduce(lambda x, y: x * y, [getattr(max_values, color) for color in ["red", "green", "blue"]])


def read_input(file_name: str) -> list[str]:
    with open(file_name) as f:
        return f.read().splitlines()


def parse_games(input_list: list[str]) -> list[Game]:
    games: list[Game] = []
    for line in input_list:
        match: Match[str] | None = re.search(r"(\d+)", line)
        if match is not None:
            games.append(Game(id=int(match.group(0)), original_input=line))
    return games


def find_color_value(round_string: str, color: str) -> int:
    """Find and return the value for a given color in the round string."""
    match = re.search(rf"(\d+) {color}", round_string)
    return int(match.group(1)) if match else 0


def parse_rounds(line: str) -> list[Round]:
    """Parse a line of input into a list of Rounds, return for adding to an existing Game"""
    rounds: list[Round] = []
    # use the regex pattern = r'(\w+): (\d+)' # this says "match any word, then a colon, then a space, then a number"
    # to remove this
    line = strip_game_id(line)
    # now break it up into a list of rounds by splittin on semicolon
    round_string_list: list[str] = line.split(";")

    for round_string in round_string_list:
        red = find_color_value(round_string, "red")
        green = find_color_value(round_string, "green")
        blue = find_color_value(round_string, "blue")
        rounds.append(Round(red=red, green=green, blue=blue))

    return rounds


def strip_game_id(line: str) -> str:
    """Remove the game id from the line of input"""
    # use the regex pattern = r'(\w+): (\d+)' # this says "match any word, then a colon, then a space, then a number"
    return re.sub(r"(\w+) (\d+): ", "", line)


def main():
    args = sys.argv[1:]  # assume first arg is file name
    file_name = args[0]

    max_values: MaxValues = MaxValues(red=12, green=13, blue=14)

    input_list = read_input(file_name)
    games: list[Game] = parse_games(input_list)

    for game in games:
        game.rounds = parse_rounds(game.original_input)

    power_sum = reduce(lambda x, y: x + y, map(lambda x: x.get_power(), games))
    print(power_sum)


if __name__ == "__main__":
    main()
