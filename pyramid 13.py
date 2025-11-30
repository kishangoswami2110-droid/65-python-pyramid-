nums = [1,3,5,7,9]
for i in range(5, 0, -1):
    for j in range(i):
        print(nums[j], end="")
    print()
