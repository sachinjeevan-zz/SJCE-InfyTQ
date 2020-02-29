x=list(map(int,input().split(" ")))
x.insert(0,-1)
heap = [-1]
for i in range(1,len(x)):
    heap.append(x[i])
    k=i
    while(k//2>0):
        if(heap[k]>heap[k//2]):
            heap[k],heap[k//2]=heap[k//2],heap[k]
            k=k//2
        else:
            break
print(*heap[1:])
length = len(x)-1
while(length>1):
    heap[1],heap[length]=heap[length],heap[1]
    k=1
    length-=1
    while(2*k<=length):
        if(2*k+1<=length):
            ind = 2*k+1 if(heap[2*k+1]>heap[2*k]) else 2*k
            if(heap[ind]>heap[k]):
                heap[ind],heap[k]=heap[k],heap[ind]
                k=ind
            else:
                break
        else:
            if(heap[2*k]>heap[k]):
                heap[k],heap[2*k]=heap[2*k],heap[k]
                k = 2*k
            else:
                break
print(*heap[1:])