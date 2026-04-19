from math import ceil, log2
from pathlib import Path


def min_number_of_drops(n: int, h: int) -> int:
    if n >= ceil(log2(h + 1)):
        return ceil(log2(h + 1))

    # dp[drops][devices]
    dp = [[0] * (n + 1) for _ in range(h + 1)]

    drops = 0
    while dp[drops][n] < h:
        drops += 1
        for devices in range(1, n + 1):
            # ellenőrizhető szintek -> szintek alatta (törik) + szintek felette (nem törik) + 1 (jelenlegi szint)
            dp[drops][devices] = dp[drops - 1][devices - 1] + dp[drops - 1][devices] + 1

    return drops


def main():
    data = Path("input.txt").read_text(encoding="utf-8")

    for line in data.splitlines():
        n, h = line.split(",")
        result = min_number_of_drops(int(n), int(h))
        print(result)


if __name__ == "__main__":
    main()
