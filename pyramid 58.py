n = 5
for i in range(1, n+1):
    print("  " * (n-i), end="")
    vals = list(range(i, i+i)) + list(range(i+i-2, i-1, -1))
    print(" ".join(str(v) for v in vals))