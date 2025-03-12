x = int(input("x-coordinate: "))
y = int(input(" y-coordinate: "))

if x > 0 and y > 0:
    print("First quadrant")
elif x < 0 and y > 0:
    print("Second quadrant")
elif x < 0 and y < 0:
    print("Third quadrant")
elif x > 0 and y < 0:
    print("Fourth quadrant")
elif x == 0 and y != 0:
    print("On y-axis")
elif x != 0 and y == 0:
    print("On x-axis")
else:
    print("Origin")