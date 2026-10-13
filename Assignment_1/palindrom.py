print("enter no you want to check palindrome \n")
n=int(input("enter no : "))

def is_palindrome_number(n):
   return str(n) == str(n)[::-1]
print(is_palindrome_number(n))
