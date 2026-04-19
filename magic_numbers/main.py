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

    # már magic number-e (stringként a megfordítás miatt)
    if number_string == number_string[::-1]:
        return number

    is_odd = length % 2 != 0
    half_length = length // 2

    left = number_string[:half_length]
    middle = number_string[half_length] if is_odd else ""

    mirrored = left + middle + left[::-1]

    if int(mirrored) >= number:
        return int(mirrored)

    left_middle_value = int(left + middle) + 1
    new_left_middle = str(left_middle_value)

    if is_odd:
        new_left = new_left_middle[:-1]
        new_middle = new_left_middle[-1]
        return int(new_left + new_middle + new_left[::-1])
    else:
        return int(new_left_middle + new_left_middle[::-1])


def main():
    data = Path("input.txt").read_text(encoding="utf-8")

    for line in data.splitlines():
        number = parse_input(line)
        magic_number = next_magic_number(number)

        print(magic_number)


if __name__ == "__main__":
    main()
