print("grading system \n")

num1=int(input("enter your marks : "))
if(num1>=95):
    print("yu got O grade")
elif(num1>90 and num1<=95):
    print("you got A+ grade")
elif(num1>80 and num1<90):
    print("A grade")
elif(num1>75 and num1<80):
    print("you got B+ grade")
elif(num1>70 and num1<75):
    print("you got B grade")
else:
    print("fail")