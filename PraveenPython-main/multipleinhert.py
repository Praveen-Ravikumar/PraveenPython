# multiple inhertance which has many base classes and one derived class
#base classes
class A:
    def __init__(self): # construtor
        print("A constructor")
class B:
    def funB(self):
        print("B selffunction")

#derived class C
class C(A, B):
    def funC(self):
        print("C derived class")

# function class 
call=C()     # A constructor
call.funB() # B selffunction
call.funC()# C derived class

