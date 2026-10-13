print("Welcome to Compund Interest Calculator\n")
P = float(input("Enter principal amount: "))
R = float(input("Enter annual interest rate (%): "))
N = int(input("Enter times interest is compounded per year: "))
T = float(input("Enter time in years: "))

R = R / 100
A = P * (1 + R / N) ** (N * T)
interest = A - P
print(f"\nFinal Amount: {A:.2f}")
print(f"Interest Earned: {interest:.2f}")
