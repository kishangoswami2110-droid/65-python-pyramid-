rows = 5
for i in range(rows, 0, -1):
    ch = "*" if i % 2 != 0 else "#"
    print((ch + " ") * i)
