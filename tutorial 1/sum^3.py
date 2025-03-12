n = int(input("enter a +ve no: "))
c_sum = 0

for i in range(2, n+1, 2):
    c = i**3
    c_sum += c

print(f"sum   of cubes of even numbers  {c_sum}")