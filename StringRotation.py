s,t=input().split(":")
t=t.strip()
x = list(map(lambda a: int(a)**2,t))
x=sum(x)
if(x%2==0):
    print(s[-1]+s[0:-1])
else:
    print(s[2:]+s[0:2])