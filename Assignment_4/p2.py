import numpy as np
df=np.array([23,22,44,54,67,33,68,33,41,98])
print(df)
print(f"First element is {df[0]} and last element is {df[len(df)-1]}")
print(f"First 5 element are {df[0:5]} last 3 element are {df[len(df)-1:len(df)-4:-1]}")

print(f"element from index 2 to 7 are {df[2:8]}")
print(f"alternative element even {df[::2]}")
print(f"alternative element odd {df[1::1]}")
print(f"Reversing element {df[::-1]}")