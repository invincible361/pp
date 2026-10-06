t=(1,2,3,4,5,6,767,8,9,0,7,5,34)
d=(4,3,2,2,3,3)
concat=t+d
print(concat)
print("differnet way of slicing")
print("all value positive ",concat[1:3:1])
print("positive start stop but negative step ",concat[1:3:-1])
print("negative start with positive end and step ",concat[-1:3:1])
print("negative start and step with positive end ",concat[-1:3:-1])
print("Negative start stop qands step ",concat[-1:-3:-1])
print("negative start stop with positive step by default ",concat[-1:-3])
print("positive start with negative end and step ",concat[1:-3:-1])


print("element at index 2 :",concat[2])




