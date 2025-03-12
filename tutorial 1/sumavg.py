num1 = int(input("first integer: "))
num2 = int(input("second integer: "))
num3 = int(input("third integer: "))
num4 = int(input("fourth integer: "))

numbers = [num1, num2, num3, num4]
pos_sum = 0
neg_sum = 0
pos_count = 0
neg_count = 0

for num in numbers:
    if num > 0:
        pos_sum += num
        pos_count += 1
    elif num < 0:
        neg_sum += num
        neg_count += 1

pos_avg = pos_sum / pos_count if pos_count > 0 else 0
neg_avg = neg_sum / neg_count if neg_count > 0 else 0

print(f"Sum of +ve numbers: {pos_sum}")
print(f"Sum of -ve numbers: {neg_sum}")
print(f"avg of +ve numbers: {pos_avg}")
print(f"avg of -ve numbers: {neg_avg}")