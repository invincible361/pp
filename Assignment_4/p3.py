import numpy as np
df=np.array([23,22,21,34,56,66,22,87,22])
df2=np.array([67,65,33,21,11,22,44,73,22])
print(f"Internal marks 1 {df}\nInternal marks 2 {df2}")
print(f"Adition of array index wise {df+df2}")

print(f"Subtraction of array index wise {df-df2}")

print(f"Multiplication of array index wise {df*df2}")

print(f"Division of array index wise {df/df2}")


print(f"Average of Interenal marks 1 {df.sum()/len(df)}")
print(f"Average of Interenal marks 2 {df2.sum()/len(df2)}")