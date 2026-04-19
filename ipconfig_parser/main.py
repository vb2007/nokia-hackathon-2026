from json import dump
from pathlib import Path

def format_line(line: str) -> str:
    formatted_line = line.replace(".", "").strip().lower()
    return formatted_line.replace(" ", "_").replace("-", "_")

def ipconfig_parser(file_name: str, lines: list[str]) -> dict:
    output = []

    for path

def main():
    final_output = []

    for path in sorted(Path(".").glob("*.txt")):
        with open(path, "r", encoding="utf-8", errors="replace") as file:
            lines = file.readlines()

        parsed_data = ipconfig_parser(path.name, lines)
        if parsed_data:
            final_output.append(parsed_data)

    with open("output_simple.json", "w", encoding="utf-8") as file:
        dump(final_output, file, indent=4)


if __name__ == "__main__":
    main()
