lower = int(input("enter lower"))
upper = int(input("enter upper"))
o_sum = 0

for num in range(lower, upper + 1):
    if num % 2 != 0:
        o_sum += num

print(f"sum = {o_sum}")