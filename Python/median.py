with open("numbers.txt", 'r') as fp:
    nums = list(map(int, fp.readlines()))

print(nums)
nums.sort()

if (n := len(nums)) % 2 == 0:
    med = (nums[n // 2] + nums[n // 2 + 1]) / 2
else:
    med = nums[n // 2]

print(f"Median: {med}")
