from pathlib import Path


def next_magic_number(n):
    n += 1

    while True:
        s = str(n)
        if s == s[::-1]:
            return n
        else:
            n += 1


def main():
    data = Path("input.txt").read_text(encoding="utf-8")

    for line in data.splitlines():
        n = int(line.strip())
        magic_number = next_magic_number(n)
        print(magic_number, end="")


if __name__ == "__main__":
    main()
