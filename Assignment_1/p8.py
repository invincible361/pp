print("Welcome to Table class\n")
n=int(input("enter number whose table you wantr to see"))
end=int(input("till where you want to see that table : "))
for i in range(end+1):
    print(f"{n} * {i} = {i*n}")