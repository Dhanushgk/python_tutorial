num = input("enter a number: ")
digits = len(num)
num_int = int(num)
total = 0

for digit in num:
    total += int(digit) ** digits

if total == num_int:
    print(f"{num_int} is an arm number")
else:
    print(f"{num_int} is not an arm number")