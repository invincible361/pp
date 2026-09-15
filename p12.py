import math
print("welcome to prime series display\n")
start=int(input("enmter from where you want to see prime no"))
end=int(input("enter till where you weant to see prime no"))

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True


print(f"prime no from {start } to {end } are:\n")
for num in range(start,end+1):
    if is_prime(num):
        print(num)
    continue