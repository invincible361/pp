t=(1,2,3,4,5,6,767,8,9,0,7,5,34)
d=(4,3,2,2,3,3)
print(f"before swapping value of t1 {t} \nwith value {id(t)} \n and t2 {d} with id \n{id(d)}")
t,d=d,t
print(f"after swapping value of t1 {t}\n with value {id(t)} \n and t2 {d}\n with id {id(d)}")
