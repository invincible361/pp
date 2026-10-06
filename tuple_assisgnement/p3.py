t=(1,2,3,4,5,6,767,8,0,0,0,9,0,7,5,34)
d=(4,3,2,2,3,3)
concat=t+d
print(concat)
count_dict=dict()
for i in concat:
    if i in count_dict.keys():
        count_dict[i]+=1
    else:
        count_dict[i]=1
for i,j in count_dict.items():
    print(f" Number {i} appeared : {j}")