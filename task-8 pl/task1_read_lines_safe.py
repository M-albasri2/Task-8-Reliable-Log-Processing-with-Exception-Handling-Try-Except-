# Task 1 — Safe File Reading (Try/Except)

from pathlib import Path

def read_lines_safe(path: str) -> list[str]:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content.splitlines()
    except FileNotFoundError:
        print(f"ERROR: File not found: {path}")
        return []
    except Exception as e:
        print(f"ERROR: Could not read file: {e}")
        return []

def main():
    # Test 1: missing file
    missing = read_lines_safe("this_file_does_not_exist.txt")
    print("Missing file lines:", len(missing))

    # Test 2: existing file
    existing = read_lines_safe("sample_logs_exception.txt")
    print("Existing file lines:", len(existing))

if __name__ == "__main__":
    main()
