n = int(input("enter numbers"))
e_count = 0
o_count = 0

for i in range(n):
    num = int(input(f"enter number {i+1}: "))
    if num % 2 == 0:
        e_count += 1
    else:
        o_count += 1

print(f"Count of even numbers: {e_count}")
print(f"Count of odd numbers: {o_count}")