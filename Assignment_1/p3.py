# print("Hello \n welcome to python Calculator \n")
# num1=int(input("enter 1st no : "))
# num2=int(input("enter 2nd no :  "))
while True:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\nHello \n welcome to python Calculator \n")
    num1=int(input("enter 1st no : "))
    num2=int(input("enter 2nd no :  "))
    print("you can perform following operation \n 1. + \n 2. - \n 3. / \n 4. *\n")

    operator=input("enter operator you wanna perform : ")
    match operator:
        case "+":
            print(f"addition of {num1 } and {num2 } is {num1+num2}")
        case "-":
                print(f"subtraction of {num1 } and {num2 } is {num1-num2}")
        case "*":
                    print(f"Multiplication of {num1 } and {num2 } is {num1*num2}")
        case "/":
                print(f"division of {num1 } and {num2 } is {num1/num2}")
    ch=input("Do you want to continue using this calculator?(Y/N): ")
    if(ch=="Y"):
        continue
    else:
        print("Exiting Program\n Thank you")
        break