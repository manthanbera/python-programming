import time
from functools import lru_cache, wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print("Time taken:", end - start)

        return result

    return wrapper


# Manual Memoization
@timer
def fibonacci_manual(n):
    memo = [-1] * (n + 1)

    memo[0] = 0
    if n > 0:
        memo[1] = 1

    def fibonacci(n):
        if memo[n] != -1:
            return memo[n]

        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return memo[n]

    return fibonacci(n)


# LRU Cache
@lru_cache(maxsize=None)
def fibonacci_lru_cached(n):
    if n <= 1:
        return n

    return fibonacci_lru_cached(n - 1) + fibonacci_lru_cached(n - 2)


@timer
def fibonacci_lru(n):
    return fibonacci_lru_cached(n)

n = int(input("Enter n: "))

print("\nManual Memoization:")
result1 = fibonacci_manual(n)
print(f"F({n}) = {result1}")

print("\nLRU Cache:")
result2 = fibonacci_lru(n)
print(f"F({n}) = {result2}")
