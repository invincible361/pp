li=[]
while True:
    ele=int(input("eneter element: "))
    li.append(ele)
    ch=int(input("do you want to add more (0/1): "))
    if ch==0:
        break
l=[x*x for x in li]
t=tuple(l)
print(t,"\n stored user info in list \n then used list comprehension for squaring \n converted to tuple \n",type(t))