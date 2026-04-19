from json import dump
from pathlib import Path


def format_line(line: str) -> str:
    formatted_line = line.replace(".", "").strip().lower()
    return formatted_line.replace(" ", "_").replace("-", "_")


def ipconfig_parser(file_name: str, lines: list[str]) -> dict:
    output = {"file_name": file_name, "adapters": []}
    current_adapter = None

    for line in lines:
        line = line.rstrip("\n")

        # új adapter kezelése
        if not line.startswith(" ") and line.endswith(":"):
            if "Windows IP Configuration" not in line:
                current_adapter = {"adapter_name": line[:-1].strip()}
                output["adapters"].append(current_adapter)

        # kulcs-érték párok kezelése
        elif ":" in line and current_adapter is not None:
            key_part, val_part = line.split(":", 1)
            key = format_line(key_part)
            val = val_part.split("(")[0].strip()
            current_adapter[key] = val

    # Only return if we actually found adapters
    return output if output["adapters"] else None


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
