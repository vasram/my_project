list=[]
n=int(input("enter the array size"))
for i in range(n):
    list.append(int(input("enter the num")))

print(list)
l,r=0,n-1

while l<r:
    # print(list[l]," ",list[r])
    list[l],list[r]=list[r],list[l]
    l=+1
    r=-1
print(list)
