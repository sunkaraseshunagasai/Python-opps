#super class and subclass has same method. if we acccess the method in subclass then only subclass method is accessed without accessing superclass method
#Already created a method in superclass then implementing the same method in subclass with different logic
#and accessing in subclass.if it overrides superclass method then it is called method overriding.
#RULES FOR METHOD OVERRIDING
#1.superclass & subclass must be present
#2.Declare two classes with same method & same parameters
#3.logic must be different in methods
# 4.Method overriding will done when we access the samemethod in subclass.if we access in superclass then override do not work
#let's see a basic example:
# class parent:
#     def method(self):
#         print('iam parent')
# class child(parent):
#     def method(self):
#         print('iam child')
# c=child()
# c.method()
#----------------------------------------
class parent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class child(parent):
    def __init__(self,a,b,c,d):
        self.c=c
        self.d=d
        parent.__init__(self,a,b)
    def add(self):
        print(self.a+self.b+self.c+self.d)
        
c=child(1,2,3,4)
c.add()