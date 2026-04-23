# Task 3 — Process File + Print Stats

from task1_read_lines_safe import read_lines_safe
from task2_parse_validate import parse_and_validate_line

def main():
    lines = read_lines_safe("sample_logs_exception.txt")
    loaded = len(lines)
    valid = 0
    invalid = 0

    for line in lines:
        result = parse_and_validate_line(line)
        if result is None:
            invalid += 1
        else:
            valid += 1

    print(f"Loaded: {loaded}")
    print(f"Valid: {valid}")
    print(f"Invalid: {invalid}")

if __name__ == "__main__":
    main()
