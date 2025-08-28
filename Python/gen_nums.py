from random import randint


nums = [randint(0, 500) for _ in range(100)]

with open("numbers.txt", 'w') as fp:
    for n in nums:
        fp.write(str(n))
        fp.write('\n')
