import string

letters = iter(string.ascii_uppercase)
num = 1

for row in range(1, 6):
    line = []
    for col in range(row):
        if (row + col) % 2 == 0:
            line.append(next(letters))
        else:
            line.append(str(num))
            num += 1
    print(" ".join(line))