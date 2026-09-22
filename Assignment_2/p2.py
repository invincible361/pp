l=[]
while True:
    ch=int(input("enter your choice\n 1. to add element to list \n 2. to sory list \n 3. to search for sepcific index"))
    if ch==1:
        ele=int(input("enter element you want to add"))
        l.append(ele)
        print(l)
    elif(ch==2):
        l.sort()
        print(l)
    elif(ch==3):
        search=int(input("enter element you want to search in list"))
        if(search in l):
            print(" it is present at this index ",l.index(search))
        else:
            print("element not found")
        