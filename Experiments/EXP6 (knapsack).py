def knapsack_bottom_up(values, weights, W):
    n = len(values)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][W]

def knapsack_top_down(values, weights, W):
    n = len(values)
    memo = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]

    def knapsack_recursive(i, w):
        if i == 0 or w == 0:
            return 0
        if memo[i][w] != -1:
            return memo[i][w]
        if weights[i - 1] <= w:
            memo[i][w] = max(
                knapsack_recursive(i - 1, w),
                knapsack_recursive(i - 1, w - weights[i - 1]) + values[i - 1]
            )
        else:
            memo[i][w] = knapsack_recursive(i - 1, w)
        return memo[i][w]

    return knapsack_recursive(n, W)

if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    W = 50

    print("Bottom-up approach:", knapsack_bottom_up(values, weights, W))
    print("Top-down approach:", knapsack_top_down(values, weights, W))