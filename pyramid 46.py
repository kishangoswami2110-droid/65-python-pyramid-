def pattern46():
    s = "1#3#5"
    for i in range(len(s)):
        print(" " * (2 * (len(s)-i-1)) + s[i:])

pattern46()