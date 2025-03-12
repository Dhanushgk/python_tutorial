import math

a = int(input("enter coefficient a: "))
b = int(input("enter coefficient b: "))
c = int(input("enter coefficient c: "))

dis = b*b - 4*a*c

if dis > 0:
    root1 = (-b + math.sqrt(dis)) / (2*a)
    root2 = (-b - math.sqrt(dis)) / (2*a)
    print(f"Roots are {root1} and {root2}")
elif dis == 0:
    root = -b / (2*a)
    print(f"Root is {root}")
else:
    real = -b / (2*a)
    imaginary = math.sqrt(abs(dis)) / (2*a)
    print(f"{real}+{imaginary}i {real}-{imaginary}i")