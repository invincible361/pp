import numpy as np
df=np.array([1,2,3,4,5,6,7,8,9,0])
print("The array initialized is ",df)
print(f"shape {df.shape}\n size {df.size}\n Dimension {df.ndim}\n Datatype {df.dtype}")

row=int(input("Row you want to reshape "))
column=int(input("Column you want to reshape "))

newdf=df.reshape(row,column)
print("2-D array",newdf)
print(f"Shape {newdf.ndim}")