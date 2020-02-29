a=list(map(int,input().split(" ")))
max_so_far = a[0]+a[1]
x=[a[0],a[1]]
mat=[]
i=2
while(i<len(a)):
    if(max_so_far==a[i]):
        x.append(a[i])
        max_so_far=a[i]+a[i-1]
    else:
        max_so_far=a[i]+a[i-1]
        if(len(x)>=3):
            mat.append(x)
        x=[a[i-1],a[i]]
    i+=1
if(len(x)>=3):
    mat.append(x)
print(mat)
