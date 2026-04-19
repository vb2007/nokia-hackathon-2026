from datetime import datetime
from pathlib import Path


def calculate_fee(entry: str, exit: str) -> int:
    fmt = "%Y-%m-%d %H:%M:%S"
    entry_time = datetime.strptime(entry, fmt)
    exit_time = datetime.strptime(exit, fmt)

    # teljes időtartam percekben
    duration_mins = (exit_time - entry_time).total_seconds() / 60

    # első 30p ingyenes
    if duration_mins <= 30:
        return 0

    days = int(duration_mins // 1440)  # 1440 perc = 24 óra
    remaining_mins = duration_mins % 1440

    total_fee = days * 10000
    remainder_fee = 0

    if remaining_mins <= 180:  # 3 óráig
        remainder_fee = remaining_mins * 5  # 300ft / 60p = 5
    else:
        # első 3ó 5 ft/perc, utána 8.33 ft/perc (500/60)
        remainder_fee = (180 * 5) + ((remaining_mins - 180) * (500 / 60))

    # egy nap nem lehet több mint 10000 ft
    if remainder_fee > 10000:
        remainder_fee = 10000

    total_fee += remainder_fee

    return int(round(total_fee))


def process_data(data: str) -> str:
    lines = data.strip().split("\n")
    output_lines = []

    # 2 header átugrása
    for line in lines[2:]:
        if not line.strip():
            continue

        parts = line.split()

        entry = f"{parts[1]} {parts[2]}"
        exit_t = f"{parts[3]} {parts[4]}"

        fee = calculate_fee(entry, exit_t)

        output_lines.append(str(fee))

    return "\n".join(output_lines) + "\n"


def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    result = process_data(data)
    print(result, end="")


if __name__ == "__main__":
    main()
