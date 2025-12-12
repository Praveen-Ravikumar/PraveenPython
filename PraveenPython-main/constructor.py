# default constructor
# the __init__ method is used in the constructor, which is inbuilt funtion defualt doesnt pass any 
#arguments

class emp():
    def __init__(self):
        print("hello world!")
e=emp()

# constructor with arguments 
class emy:
    def __init__(self,a,b):
        self.A=a
        self.B=b
    def add(self):
        print("the additon of the two arguments is:",self.A+self.B)
d=emy(2,3)
d.add()