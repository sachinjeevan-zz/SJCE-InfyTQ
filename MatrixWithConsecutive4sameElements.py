m=int(input())
mat=[list(map(int,input().split(" "))) for i in range(m)]
n=len(mat[0])
min_so_far = 9999999999999999999999
for i in range(0,m):
    for j in range(0,n):
        if(i+3<m):
            s = [mat[i][j],mat[i+1][j],mat[i+2][j],mat[i+3][j]]
            s=list(set(s))
            if(len(s)==1):
                min_so_far = s[0] if(s[0]<min_so_far) else min_so_far
                continue
        if(j+3<n):
            s=mat[i][j:j+4]
            s=list(set(s))
            if(len(s)==1):
                min_so_far = s[0] if(s[0]<min_so_far) else min_so_far
                continue
        if(i+3<m and j+3<n):
            s=[mat[i][j],mat[i+1][j+1],mat[i+2][j+2],mat[i+3][j+3]]
            s=list(set(s))
            if(len(s)==1):
                min_so_far = s[0] if(s[0]<min_so_far) else min_so_far
                continue
        if(i+3<m and j-3>=0):
            s=[mat[i][j],mat[i+1][j-1],mat[i+2][j-2],mat[i+3][j-3]]
            s=list(set(s))
            if(len(s)==1):
                min_so_far = s[0] if(s[0]<min_so_far) else min_so_far
                continue
min_so_far = -1 if min_so_far==9999999999999999999999 else min_so_far
print(min_so_far)