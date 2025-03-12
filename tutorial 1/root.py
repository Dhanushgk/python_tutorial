import math

a = int(input("Enter coefficient a: ")) 
b = int(input("Enter coefficient b: "))


c = int(input("Enter coefficient c: "))


dis = b*b - 4*a*c



if dis > 0:
    root1 = (-b + math.sqrt(dis)) / (2*a)
    root2 = (-b - math.sqrt(dis)) / (2*a)
    print(f"Two distinct roots: {root1} and {root2}")
elif dis == 0:
    root = -b / (2*a)
    print(f"One repeated root: {root}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(dis)) / (2*a)
    print(f"Complex roots: {real_part}+ {imaginary_part}i and {real_part}  -{imaginary_part}i")