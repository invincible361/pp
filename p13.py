print("to check armstrong no \n")
num = int(input("Enter a number: "))
order = len(str(num))
total = 0
temp = num
while temp > 0:
   digit = temp % 10
   total += digit ** order
   temp //= 10
if num == total:
   print(f"{num} is an Armstrong number")
else:
   print(f"{num} is not an Armstrong number")