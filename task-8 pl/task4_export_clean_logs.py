# Task 4 — Export Clean Logs File

from pathlib import Path
from task1_read_lines_safe import read_lines_safe
from task2_parse_validate import parse_and_validate_line

OUT_PATH = Path("clean_logs_exception.txt")

def main():
    lines = read_lines_safe("sample_logs_exception.txt")
    clean_lines = []

    for line in lines:
        parsed = parse_and_validate_line(line)
        if parsed is None:
            continue
        ts, lvl, svc, msg = parsed
        clean_lines.append(f"{ts} | {lvl} | {svc} | {msg}")

    OUT_PATH.write_text("\n".join(clean_lines), encoding="utf-8")
    print(f"Wrote {len(clean_lines)} clean lines to {OUT_PATH}")

if __name__ == "__main__":
    main()
