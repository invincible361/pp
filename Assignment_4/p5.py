import numpy as np
df=np.array([
    [22,33,11,44,56],[22,33,13,45,55],[66,43,11,76,54],[53,44,21,44,55],[76,43,45,65,32],[14,64,22,44,22]
])
print("student marks",df)
print("Sum of there marks ",df.sum(axis=1))#axis 1 means to sum row wise horizontal 

average=df.sum(axis=1)/5
print(f"Average marks of each student {average}")
highest=df.max()
print(f"Highest marks among all student and subject is {highest}")
lowest=df.min()
print(f"Lowest marks among all student and subject is {lowest}")
avera=df.sum()/(df.size)
print(avera)
# highgest
# lowerst
# overal average subject wise total
print("subject wise total marks",df)
print(df.sum(axis=0))#axis 1 means to sum row wise horizontal 
