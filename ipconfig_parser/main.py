from pathlib import Path


def format_line(line: str) -> str:
    formatted_line = line.replace(".", "").strip().lower()
    return formatted_line.replace(" ", "_").replace("-", "_")


def main():
    for path in sorted(Path(".").glob("*.txt")):
        print(path.name)


if __name__ == "__main__":
    main()
