l=[]
while True:
    ch=int(input("Enter choice: \n 1. to add element at end of list \n 2. to add at specific location \n 3 to delete specific element \n 4 to delete specific index \n other no to exit program"))
    if ch==1:
        ele=input("Enter element you want to add: ")
        l.append(ele)
        print(l)
    elif(ch==2):
        ele=input("Enter element you want to add: ")
        pos=int(input("Enter position you want to add element: "))
        l.insert(pos,ele)
        print(l)
    elif(ch==3):
        ele=input("Enter element you want to add: ")
        l.remove(ele)
        print(l)
    elif(ch==4):
        pos=int(input("Enter index location to delete element: "))
        l.pop(pos)
        print(l)

    else:
        break
        
    
    