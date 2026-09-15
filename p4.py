print("Hello \n Enter value for two variable")
a=input("Enter text or no here ")
b=input("Enter text or no here ")
print("\n before swapping \n")


print(id(a),"is location where we store ",a)
print(id(b),"is location where we store ",b)
a,b=b,a


print("after swapping\n")
print(id(a),"is location where we store ",a)
print(id(b),"s location where we store ",b)

