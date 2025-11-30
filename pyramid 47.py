def pattern47():
    parts = ["1", "#", "3", "#", "5"]
    for i in range(5):
        print(" " * (2 * i) + " ".join(parts[:5-i]))

pattern47()