first = int(input("Enter first number: "))


second = int(input("Enter second number: "))

if first > second:
    print(f"{first} is greater than {second}")
elif second > first:
    print(f"{second} is greater than {first}")
else:

    print("Both numbers are equal")