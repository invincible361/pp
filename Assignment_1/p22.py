a=int(input("Enter first no: "))
b=int(input("Enter second no: "))
while b!=0:
    rem=a%b
    a=b
    b=rem
print(f"GCD of {a} and {b} is {rem}")