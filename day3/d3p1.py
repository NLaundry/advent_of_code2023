import re
import sys
from os import read
from dataclasses import dataclass
from functools import reduce

# pattern_not_period = r"[!#$%&'()*+,-/:;<=>?@[\\\]^_`{|}~]"
pattern_not_period = r"[!#$%&'()*+\-,:;<=>?@[\\\]^_`{|}~\/]"

@dataclass
class Symbol:
    x_coord: int
    y_coord: int
    symbol: str


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
        return f"PartNumber: {self.part_number}   x_left_coord: {self.x_left_coord}, x_right_coord: {self.x_right_coord}, y_coord: {self.y_coord}"
    
    def has_collision(self, symbol_list: list[Symbol]) -> bool:
        possible_symbol_collisions = list(filter(lambda symbol: symbol.y_coord in range(self.y_coord - 1, self.y_coord +2), symbol_list))
        return any(symbol.x_coord in range(self.x_left_coord -1, self.x_right_coord +2) for symbol in possible_symbol_collisions)

    # def has_collision_test(self, symbol_list: list[Symbol]) -> list[Symbol]:
    #     possible_symbol_collisions = list(filter(lambda symbol: symbol.y_coord in range(self.y_coord - 1, self.y_coord +2), symbol_list))
    #     return [ symbol for symbol in possible_symbol_collisions if symbol.x_coord in range(self.x_left_coord -1, self.x_right_coord +2) ]



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
                x_right_coord=match.end() -1, #match.end gets the index of the character RIGHT AFTER THE LAST CHARACTER IN THE MATCH
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
    parts:  list[PartNumber]  = []
    symbols: list[Symbol] = []
    for line in lines:
        symbols.extend(parse_symbols_for_line(line, lines.index(line)))
        parts.extend(parse_part_number_for_line(line, lines.index(line)))

    # for part in parts:
    #     print(part)
    #     print(part.has_collision_test(symbols))
    #     print(part.has_collision(symbols))

    parts_with_collisions = list(filter(lambda part: part.has_collision(symbols), parts))
    part_sum = reduce(lambda x, y: x + int(y.part_number), parts_with_collisions, 0)
    print(part_sum)


if __name__ == "__main__":
    main()
