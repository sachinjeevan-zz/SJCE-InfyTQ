class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(one,two):
        return one.b * two.a
obj1 = Test(10,70)
obj2 = Test(20,80)
print(obj1 + obj2)