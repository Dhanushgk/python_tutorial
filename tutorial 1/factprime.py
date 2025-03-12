n = int(input("enter a number: "))
og = n
fact = []

i = 2
while i * i <= n:
    if n % i:
        i += 1
    else:
        n //= i
        fact.append(i)

if n > 1:
    fact.append(n)

print(f"Prime factors of {og}: {fact}")