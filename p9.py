print("welcome to factorial calculator \n")
factno=int(input("enter no whose factorial you want : "))

def fact( n):
    if(n ==1):
        return 1
    else:
        return n*fact(n-1)
    
print(f"factorial of {factno } is {fact(factno)}")          