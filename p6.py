print("this program will tell which no out of three is bigger\n")

a=int(input("enter no "))
b=int(input("enter no "))
c=int(input("enter no "))
if(a>b and a>c):
    print(f"{a} is bigesst among three")
elif(b>a and b>c):
    print(f"{b} is biggest")
else:
    print(f"{c}is biggest")

# print(max(a,b,c))