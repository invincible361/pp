print("Welcome to Leap year checker\n")

year=int(input("enter year you want to check : "))
if(year%4==0 and year%100!=0 )or (year%400==0 ):
    print(f"Yes {year} is leap year")
else:print(f"{year } is not leap year")