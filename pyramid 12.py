nums = [1, 3, 5, 7, 9]
for i in range(5):
    for j in range(i, -1, -1):
        print(nums[j], end="")
    print()
