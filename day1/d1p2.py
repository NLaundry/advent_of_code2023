import regex as re
from functools import reduce

numbers = [
    # "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    # "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

word_to_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}


def convert_to_digit(num: str) -> str | None:
    if num.isdigit():
        return num
    else:
        try:
            return word_to_digit[num]
        except KeyError:
            return None

def get_lines(file_name: str) -> list:
    with open(file_name, "r") as f:
        lines = f.readlines()
        lines_stripped = list(map(lambda line: line.strip().lower(), lines))

        return lines_stripped


def find_numbers_in_order(line: str, numbers: list[str]):
    # Create a pattern that matches any of the numbers
    pattern = "|".join(number for number in numbers)
    # Find all matches in the line, preserving order
    matches = re.findall(pattern, line, overlapped=True)
    return matches


def main():
    lines = get_lines("d1p2_input.txt")
    lines_numbers = [find_numbers_in_order(line, numbers) for line in lines]
    lines_first_and_last = map(
        lambda line: [convert_to_digit(line[0]), convert_to_digit(line[-1])],
        lines_numbers,
    )
    two_digit_nums = map(lambda line: int(line[0] + line[1]), lines_first_and_last)
    sum = reduce(lambda x, y: x + y, list(two_digit_nums))
    print(sum)


if __name__ == "__main__":
    main()
