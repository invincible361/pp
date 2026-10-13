import numpy as np 
df=np.array([12,321,55,67,98,43,113])
print(f"Ascending order {np.sort(df)}\nDescending order {np.sort(df)[::-1]}")
asc=np.sort(df)
print(asc)
print(f"Highest 3 element are {asc[-4:-1]}\nlowest 3 {asc[:3]}")

print("Index value of highest element is ",np.where(df==asc[-1])[0])
