n = int(input("Enter a number: "))

factors: list[int] = []

for i in range(1, n):
    if n % i == 0:
        factors.append(i)

print(*factors, sep=", ")
