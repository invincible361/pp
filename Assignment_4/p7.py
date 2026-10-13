import numpy as np
df=np.array([
    [22,33,44,56],[22,33,13,55],[66,43,76,54],[53,44,21,55],[76,43,45,65]
])

print(df)
df=df+5
print(f"adding 5 to every student every subject marks\n Math C Python COA Seminar \n{(df)}")

bonus=[2,3,5,4]
print(df+bonus)