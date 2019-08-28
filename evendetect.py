list=[]
for i in range(1,11):
    list.append(int(input("enter the num")))
first=list[0]
for i in range(1,len(list)-1):
    lxor=first
    first=first^list[i]
    print("xor of {} and {} is = {}".format(lxor,list[i],first))
print(first)
