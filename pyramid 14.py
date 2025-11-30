nums = [9,7,5,3,1]
for i in range(5, 0, -1):
    for j in range(i):
        print(nums[j], end="")
    print()
