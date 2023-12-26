import re
import sys
from os import read
from dataclasses import dataclass
from functools import reduce

class Part:
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
        return f"Part: {self.part_number}   x_left_coord: {self.x_left_coord}, x_right_coord: {self.x_right_coord}, y_coord: {self.y_coord}"

class Gear:
    x_coord: int
    y_coord: int
    adjacent_parts: list[Part]
    is_valid: bool # True if the gear has adjacent parts

    def __init__(self, x_coord: int, y_coord: int):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def __str__(self):
        return f"Gear: x_coord: {self.x_coord}, y_coord: {self.y_coord}"

    def set_validity(self, part_list: list[Part]) -> bool:
        possible_parts = list(filter(lambda part: part.y_coord in range(self.y_coord - 1, self.y_coord +2), part_list))
        self.adjacent_parts = list(filter(lambda part: self.x_coord in range (part.x_left_coord - 1, part.x_right_coord + 2), possible_parts))
        self.is_valid = len(self.adjacent_parts) == 2 # checks if the correct number of adjacent parts were found
        return self.is_valid
    
    def calc_gear_ratio(self) -> int:
        if self.is_valid:
            return int(self.adjacent_parts[0].part_number) * int(self.adjacent_parts[1].part_number)
        else:
            return 0


def read_input(file_name: str) -> list[str]:
    with open(file_name) as f:
        return f.read().splitlines()


def parse_part_number_for_line(line: str, y_coord: int) -> list[Part]:
    part_numbers: list[Part] = []
    matches = re.finditer(r"(\d+)", line)
    for match in matches:
        part_numbers.append(
            Part(
                x_left_coord=match.start(),
                x_right_coord=match.end() -1, #match.end gets the index of the character RIGHT AFTER THE LAST CHARACTER IN THE MATCH
                y_coord=y_coord,
                part_number=match.group(0),
            )
        )
    return part_numbers

def parse_gear_for_line(line: str, y_coord: int) -> list[Gear]:
    gears: list[Gear] = []
    matches = re.finditer(r"\*", line)
    for match in matches:
        gears.append(
            Gear(
                x_coord=match.start(),
                y_coord=y_coord,
            )
        )
    return gears


def main():
    args = sys.argv[1:]  # assume first arg is file name
    file_name = args[0]
    lines = read_input(file_name)
    parts:  list[Part]  = []
    gears:  list[Gear]  = []
    for line in lines:
        gears.extend(parse_gear_for_line(line, lines.index(line)))
        parts.extend(parse_part_number_for_line(line, lines.index(line)))

    for gear in gears:
        # check for validity and assign self.valid
        gear.set_validity(parts)
        print(gear)

    valid_gears = list(filter(lambda gear: gear.is_valid, gears))
    print(valid_gears)

    gear_ratio_sum = reduce(lambda x, y: x + y.calc_gear_ratio(), valid_gears, 0)
    print(gear_ratio_sum)



if __name__ == "__main__":
    main()
