for i in range(5):
    print('  ' * i, end='')
    for j in range(5, i, -1):
        print(j, end=' ')
    print()
