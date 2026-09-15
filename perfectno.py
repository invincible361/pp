print("program to check perfect no whose sum of divisor excluding itself is equal to no ")
n = int(input("enter no you want to check perfectness : "))
Sum = 0
for i in range(1, n):
    if(n % i == 0):
        Sum = Sum + i
if (Sum == n):
    print("Number is a Perfect Number.")
else:
    print("Number is not a Perfect Number.")