import numpy as np
df=np.array([12,11,22,3443,55,34,22,40,77,96,44,35,85,34,756])
print(df)
print(f"student scoring more than 75 {df[df>75]}")
print(f"student scoring between 50 and 75 {df[(50<df) & (df<75)]}")
print(f"student scoring less than 40 {df[df<40]}")
print(f"student scoring more than 75 {(df[df>75]).size}")
df[df==40]=2
print(df)
