s=input()
s = list(filter(lambda a: a.isdigit(),s))
s=list(set(s))
s=list(map(int,s))
odd = list(filter(lambda a: a%2!=0,s))
even = list(filter(lambda a: a%2==0,s))
if(len(even)==0):
    print(-1)
else:
    even.sort()
    x = sorted(odd+even[1:],reverse=True)+[even[0]]
    print(*x,sep="")