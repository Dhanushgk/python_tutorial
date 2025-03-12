num = int(input("enter a number  "))
og = num
r_num = 0

while num > 0:
    digi = num % 10
    r_num = r_num * 10 + digi
    num //= 10

print(f"Rev of {og} is {r_num}")