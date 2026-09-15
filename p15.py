marks=int(input("enter your marks: "))
if(0<=marks<=100 ):
    if(marks>90):
        print("you got A+")
    elif(marks>80):
        print("you got A")
    elif(marks>70):
        print("you got B+")
    elif(marks>60):
        print("you got B")
    else:
        print("You got Failed /n Better luck next time")
else:
    print("invalid marks")