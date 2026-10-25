# range(start, stop, step) — stop is a cutoff, never included.

n = 4
print("range(n)           ", list(range(n)))              # 0, 1, 2, 3
print("range(0, n, 1)     ", list(range(0, n, 1)))        # same
print("range(n-1, -1, -1) ", list(range(n - 1, -1, -1)))  # 3, 2, 1, 0
