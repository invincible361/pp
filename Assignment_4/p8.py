import numpy as np
df=np.random.randint(1,101,size=(3,3))
print(f"{df} \n max emement in our random 2d array {df.max()}\n Minimum element in our 2D array {df.min()}\n Mean of value {df.sum()/df.size}\n Sorting generated values {np.sort(df)}")

greater=df[df>50]
print(f"Values greater than 50 are{greater}")