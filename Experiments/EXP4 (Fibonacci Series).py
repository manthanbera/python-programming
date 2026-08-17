n = int(input("Enter n: "))

memo = [-1] * (n + 1)
memo[0] = 0
if n > 0:
    memo[1] = 1

def fibonacci(n):
    if memo[n] != -1:
        return memo[n]

    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

print(f"F({n}) = {fibonacci(n)}")
