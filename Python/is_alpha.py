c = input("Enter any character: ")
if len(c) != 1:
    print("Enter single character")
    exit(1)

if 'a' <= c.lower() <= 'z':
    print("YES")
else:
    print("NO")
