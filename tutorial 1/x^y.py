x = float(input("enter base (X): "))
y = int(input("enter exponent (Y): "))

r = 1
for i in range(abs(y)):
    result *= x

if y < 0:
    r = 1 / r

print(f"{x}^{y} = {r}")