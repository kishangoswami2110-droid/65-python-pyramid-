n = 5
for i in range(1, n + 1):
    row = []
    for j in range(1, n + 1):
        row.append(str(max(n - j + 1, n - i + 1)))
    print(" ".join(row))
