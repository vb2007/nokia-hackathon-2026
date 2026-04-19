from pathlib import Path


def parse_input(line: str) -> int:
    line = line.strip()

    if "^" in line:  # hatványozás kezelése
        base, exp = line.split("^")
        return int(base) ** int(exp)
    return int(line)


def next_magic_number(n: int) -> int:
    n += 1

    while True:
        s = str(n)  # strnggé alakítás a fordított érték ellenőrzéséhez

        if s == s[::-1]:
            return int(n)
        n += 1


def main():
    data = Path("input.txt").read_text(encoding="utf-8")

    for line in data.splitlines():
        number = parse_input(line)
        magic_number = next_magic_number(number)

        print(magic_number)


if __name__ == "__main__":
    main()
