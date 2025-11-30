for i in range(5):
    print('  ' * i, end='')
    for j in range(5 - i):
        print(9 - 2*j, end='')
    print()