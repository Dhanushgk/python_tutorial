n = int(input("enter the value"))

for i in range(1, n+1):
    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j} = {result}")
    print()