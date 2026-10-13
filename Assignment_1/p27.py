no=int(input("enter no you want to check prime or not : "))
flag=False
for i in range(2,int(no/2)):
    if(no%i==0):
        flag=True
        print(f"{no} is composite")
        break
if flag==False:
    print(f"{no} is prime")