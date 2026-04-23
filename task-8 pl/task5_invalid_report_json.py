# Task 5 — Invalid Reason Report (JSON)

import json
from pathlib import Path
from task1_read_lines_safe import read_lines_safe

ALLOWED_LEVELS = {"INFO", "WARN", "ERROR"}
OUT_PATH = Path("invalid_report.json")

def classify_reason(line: str) -> str | None:
    # Return a reason string if invalid, or None if valid.
    s = line.strip()
    if s == "":
        return "empty_line"

    parts = [p.strip() for p in s.split("|")]
    if len(parts) != 4:
        return "invalid_format"

    ts, level, svc, msg = parts
    if ts == "" or level == "" or svc == "" or msg == "":
        return "empty_field"

    level_norm = level.upper()
    if level_norm not in ALLOWED_LEVELS:
        return "invalid_level"

    return None

def main():
    lines = read_lines_safe("sample_logs_exception.txt")
    report = {
        "invalid_format": 0,
        "empty_field": 0,
        "invalid_level": 0,
        "empty_line": 0
    }

    for line in lines:
        reason = classify_reason(line)
        if reason is not None:
            report[reason] += 1

    OUT_PATH.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("Report:", report)

if __name__ == "__main__":
    main()
