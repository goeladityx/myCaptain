mylist=[]
c= int(input("please enter the number of elements in the list: "))
for i in range(0,5):
    a= int(input())
    mylist.append(a)
newlist=[]
for num in mylist:
    if(num>0):
        newlist.append(num)
for num in newlist:
    print(num)
