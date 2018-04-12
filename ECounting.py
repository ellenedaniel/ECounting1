#Calculating number of digits and letters in a string
s = input("Input a string")
e=d=0
for c in s:
    if c.isdigit():
        e=e+1
    elif c.isalpha():
        d=d+1
    else:
        pass
print("Letters", e)
print("Digits", d)
