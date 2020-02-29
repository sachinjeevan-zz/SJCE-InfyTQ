import collections
class LFS():
    def __init__(self,x):
        self.x = x
        self.ind={}
        for a,b in enumerate(self.x):
            self.ind[b]=a
        self.maxi = -5
        self.a,self.b=-1,-1
        self.ans = collections.defaultdict(lambda:2)
        if __name__=="__main__":
            print(__name__)
    def fun(self,a,b):
        c= b-a
        if(c<a):
            self.fun(c,a)
            print(c,end=" ")
    def findLFS(self):
        for k in range(2,len(self.x)):
            for j in range(1,k):
                ele = self.x[k]-self.x[j]
                try:
                    i=self.ind[ele]
                except:
                    i=None
                if(i!=None and i<j):
                    self.ans[j,k]=self.ans[i,j]+1
                    if(self.ans[j,k]>self.maxi):
                        self.maxi = self.ans[j,k]
                        self.a,self.b=self.x[j],self.x[k]
        self.fun(self.a,self.b)
        print(self.a,self.b)

