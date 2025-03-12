count = int(input("How many numbers= "))
e_sum = 0

for i in range(count):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        e_sum += num

print(f"Sum of even numbers {e_sum}")