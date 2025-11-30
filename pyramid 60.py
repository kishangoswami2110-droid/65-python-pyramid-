n = 5
for i in range(1, n+1):
    row = []
    for j in range(1, n+1):
        row.append(str(min(j, i)))
    print(" ".join(row))