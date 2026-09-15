l=list()
flag=False
while True:
    item=input("Enter element you want5 to adds in list : ")
    l.append(item)
    print(f"Upodated list {l}")
    ch=int(input("do you want to continue adding element (0 for exit 1 for continue) "))
    if(ch==0):
        break
    else:
        continue
    
search=input("enter element you want to search in list: ")
for i in l:
    
    if(i==search):
        flag=True
        print ("item found")
        break
        
if(flag==False):
    print("not present in lsit")