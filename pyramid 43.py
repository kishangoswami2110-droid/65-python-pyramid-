def pattern43():
    num = 9
    spaces = 0
    for count in range(5, 0, -1):
        print(" " * spaces + " ".join([str(num)] * count))
        num -= 2
        spaces += 2

pattern43()