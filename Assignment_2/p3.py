l=[]
while True:
    ch=int(input("enter your choice\n 1. to add element to list \n 2. to count element \n "))
    if ch==1:
        ele=int(input("enter element you want to add: "))
        l.append(ele)
        print(l)
    if ch==2:
        freq=dict()
        for c in l:
            count=0
            for i in l:
                if(i==c):
                    count=count+1
            freq[c]=count
        for u in freq:
            print(u)