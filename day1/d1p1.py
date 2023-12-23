import re

# EXAMPLE TEXT
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

# Goal: find the sum of the first and last numbers of each line
def get_lines(file_name: str) -> list:
    with open(file_name, 'r') as f:
        lines = f.readlines()
        lines_stripped = list(map(lambda line: line.strip(), lines))
        return lines_stripped



def main():
    lines = get_lines('input_example.txt')
    print(lines)

if __name__ == '__main__':
    main()

