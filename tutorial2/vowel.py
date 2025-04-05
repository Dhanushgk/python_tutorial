def rvowels(v):
    return "".join(char for char in v if char.lower() not in "aeiou")

input_string = "Hello, World!"
print("String after removing vowels:", rvowels(input_string))
