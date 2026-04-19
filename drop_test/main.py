from math import ceil, log2
from pathlib import Path


def min_number_of_drops(n: int, h: int) -> int:
    # 1 eszköz = minden emeletet egyenként le kell tesztelni
    if n == 1:
        return h

    # ha van elég eszköz, csak ellenőrizzük binary search-el
    if n >= ceil(log2(h + 1)):
        return ceil(log2(h + 1))

    # dp = `m` dobás, `i` eszköz
    dp = [0] * (n + 1)

    drops = 0
    while dp[n] < h:
        drops += 1
        # előző dobás értékeinek használata (D-1)
        for i in range(n, 0, -1):
            dp[i] = dp[i - 1] + dp[i] + 1

    return drops


def main():
    data = Path("input.txt").read_text(encoding="utf-8")

    for line in data.splitlines():
        n, h = line.split(",")
        result = min_number_of_drops(int(n), int(h))
        print(result)


if __name__ == "__main__":
    main()
