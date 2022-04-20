m,n=map(int,input().split()); k=int(input())
li=[]
for i in range(3):
    for j in list(map(int,input().split())): 
        li.append(j)
if k in li:
    x= li.index(k)
    print("True \n",int(x/n)," ",x%n)
else:
    print("False")