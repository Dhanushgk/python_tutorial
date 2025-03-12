a = 0
b = 1
print(a, end="    ")
print(b, end=" ")

for i in range(8):
    next_num = a + b
    print(next_num, end=" ")
    a = b
    b = next_num