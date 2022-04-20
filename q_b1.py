m,n=map(int,input().split()); k=int(input())
li=list(map(int,input().split()))
if k in li:
    x= li.index(k)
    print("True \n",int(x/n)," ",x%n)
else:
    print("False")
