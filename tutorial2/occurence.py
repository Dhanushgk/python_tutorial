jk= input("Enter the string")
bub= input("Enter the substring ")

if bub in jk:
    jk = jk.replace(bub, "")
    print(jk)