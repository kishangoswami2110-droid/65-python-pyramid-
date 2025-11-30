N = 5
for i in range(1, N+1):
    print(' ' * (N - i) * 2, end='')
    for j in range(1, i+1):
        space = ' ' * (j if j < i else 0)
        print(j, end=space)
    print()