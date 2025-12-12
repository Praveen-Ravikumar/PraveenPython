class parent:
    def fun(self):
        print("parent class....")
class child(parent):
    def fun1(self):
        print("child class...")
c=child()
c.fun()
c.fun1()