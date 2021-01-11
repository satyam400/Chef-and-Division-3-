t=int(input())
l=[]
for i in range(0,t):
    n,k,d=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]

    if sum(a)<k:
        print(0)
    elif sum(a)//k<d:
        print(sum(a)//k)
    elif sum(a)//k>=d:
        print(d)



