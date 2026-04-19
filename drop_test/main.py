from pathlib import Path


def min_number_of_drops(n: int, h: int) -> int:
    # dp[devices][floors]
    dp = [[0] * (h + 1) for _ in range(n + 1)]

    for j in range(1, h + 1):
        dp[1][j] = j

    for i in range(2, n + 1):
        for j in range(1, h + 1):
            dp[i][j] = float("inf")
            for x in range(1, j + 1):
                breaks = dp[i - 1][x - 1]
                survives = dp[i][j - x]

                worst_case = 1 + max(breaks, survives)

                if worst_case < dp[i][j]:
                    dp[i][j] = worst_case

    return dp[n][h]


def main():
    data = Path("input.txt").read_text(encoding="utf-8")

    for line in data.splitlines():
        n, h = line.split()
        result = min_number_of_drops(int(n), int(h))
        print(result)

    print(data, end="")


if __name__ == "__main__":
    main()
