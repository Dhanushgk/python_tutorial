side1 = float(input("Length of first side: "))
side2 = float(input(" Length of second  side: "))
side3 = float(input("length of third side: "))

sides = [side1, side2, side3]
sides.sort()

if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print("It is a right-angled triangle")
else:
    print("It is not a right-angled triangle")