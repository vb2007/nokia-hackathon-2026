from json import dump, dumps
from pathlib import Path


def format_line(line: str) -> str:
    formatted_line = line.replace(".", "").strip().lower()
    return formatted_line.replace(" ", "_").replace("-", "_")


def ipconfig_parser(file_name: str, lines: list[str]):
    file_data = {"file_name": file_name, "adapters": []}
    current_adapter = None
    last_key = None

    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            continue

        # új adapter kezelése
        if not line.startswith(" ") and line_stripped.endswith(":"):
            if "Windows IP Configuration" not in line:
                current_adapter = {"adapter_name": line_stripped[:-1]}
                file_data["adapters"].append(current_adapter)
                last_key = None

        # kulcs-érték párok kezelése
        elif ":" in line and current_adapter is not None:
            key_part, val_part = line.split(":", 1)
            key = format_line(key_part)
            val = val_part.split("(")[0].strip()

            current_adapter[key] = [val] if val else []
            last_key = key

        elif ":" not in line and current_adapter is not None and last_key is not None:
            val = line_stripped.split("(")[0].strip()
            if val:
                current_adapter[last_key].append(val)

    for adapter in file_data["adapters"]:
        for key, val in adapter.items():
            if isinstance(val, list):
                if len(val) == 0:
                    adapter[key] = ""
                elif len(val) == 1:
                    adapter[key] = val[0]

    return file_data if file_data["adapters"] else None


def main():
    final_output = []

    for path in sorted(Path(".").glob("*.txt")):
        with open(path, "r", encoding="utf-8", errors="replace") as file:
            lines = file.readlines()

        parsed_data = ipconfig_parser(path.name, lines)
        if parsed_data:
            final_output.append(parsed_data)

    with open("output.json", "w", encoding="utf-8") as file:
        dump(final_output, file, indent=4)

    # konzolra is ki kell írni, vagy csak json fájlba?
    print(dumps(final_output, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
