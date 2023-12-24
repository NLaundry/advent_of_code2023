import re
import sys
from os import read
from dataclasses import dataclass

# pattern_not_period = r"[!#$%&'()*+,-/:;<=>?@[\\\]^_`{|}~]"
pattern_not_period = r"[!#$%&'()*+\-,:;<=>?@[\\\]^_`{|}~]"


class PartNumber:
    x_left_coord: int
    x_right_coord: int
    y_coord: int
    part_number: str

    def __init__(
        self, x_left_coord: int, x_right_coord: int, y_coord: int, part_number: str
    ):
        self.x_left_coord = x_left_coord
        self.x_right_coord = x_right_coord
        self.y_coord = y_coord
        self.part_number = part_number
    
    def __str__(self):
        return f"PartNumber: x_left_coord: {self.x_left_coord}, x_right_coord: {self.x_right_coord}, y_coord: {self.y_coord}, part_number: {self.part_number}"

@dataclass
class Symbol:
    x_coord: int
    y_coord: int
    symbol: str


def read_input(file_name: str) -> list[str]:
    with open(file_name) as f:
        return f.read().splitlines()


def parse_part_number_for_line(line: str, y_coord: int) -> list[PartNumber]:
    part_numbers: list[PartNumber] = []
    matches = re.finditer(r"(\d+)", line)
    for match in matches:
        part_numbers.append(
            PartNumber(
                x_left_coord=match.start(),
                x_right_coord=match.end(),
                y_coord=y_coord,
                part_number=match.group(0),
            )
        )
    return part_numbers

def parse_symbols_for_line(line: str, y_coord: int) -> list[Symbol]:
    symbols: list[Symbol] = []
    matches = re.finditer(pattern_not_period, line)
    for match in matches:
        symbols.append(
            Symbol(
                x_coord=match.start(),
                y_coord=y_coord,
                symbol=match.group(0),
            )
        )
    return symbols


def main():
    args = sys.argv[1:]  # assume first arg is file name
    file_name = args[0]
    lines = read_input(file_name)
    parts: list[PartNumber] = []
    symbols: list[Symbol] = []
    for line in lines:
        symbols.extend(parse_symbols_for_line(line, lines.index(line)))
        parts.extend(parse_part_number_for_line(line, lines.index(line)))
        
    for part in parts:
        print(part)
    for symbol in symbols:
        print(symbol)


if __name__ == "__main__":
    main()
