from pathlib import Path


def parse_input(line: str) -> int:
    line = line.strip()

    if "^" in line:  # hatványozás kezelése
        base, exp = line.split("^")
        return int(base) ** int(exp)
    return int(line)


def next_magic_number(number: int) -> int:
    number += 1
    number_string = str(number)
    length = len(number_string)

    # string fele: középső értékkel együtt, ha a a szám páratlan hosszú
    half = number_string[: (length + 1) // 2]

    # palindrom készítése a bal oldal tükrözésével
    # half[-2::-1] -> középső értéket tükrözi, ha páratlan
    # half[::-1] -> megtartja a középső értéket, ha páros
    candidate = int(half + (half[-2::-1] if length % 2 else half[::-1]))

    if candidate >= number:
        return candidate

    # ha kisebb volt "n"-nél, a bal oldalt 1-el növeli és újra tükröz
    half = str(int(half) + 1)
    return int(half + (half[-2::-1] if length % 2 else half[::-1]))


def main():
    data = Path("input.txt").read_text(encoding="utf-8")

    for line in data.splitlines():
        number = parse_input(line)
        magic_number = next_magic_number(number)

        print(magic_number)


if __name__ == "__main__":
    main()
