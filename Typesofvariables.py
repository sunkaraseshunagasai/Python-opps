#There are 3 types of variables 
#1.Local variable
#2.static variable or class variable
#3.instance variable
#LOCAL VARIABLE:
# the variable which is declared inside the method is called locla variable same as variable declaration in fucntion
#STATIC VARIABLE OR CLASS VARIABLE:
#The variable which is declared outside the method and inside the class then it is called class variable
#let's see an example
# class A:
#     staticvariable1=10
#     staticvariable2=20
#     def samplemethod(self):
#         print(self.staticvariable2)
#         print(A.staticvariable1)
# obj=A()
# obj.samplemethod()
# A.staticvariable1=100
# print(obj.staticvariable1)
#INSTANCE VARIABLE-------------------------------------------------------
#whenever a variable is created for object then it is instance variable
#we can access instance variable in 2 ways
# class A:
#     def __init__(self,a,b):
#         self.instancevariable1=a
#         self.instancevariable2=b
#     def updatevariable(self,newvalue):
#         self.instancevariable1=newvalue
# obj=A(10,20)
# print(obj.instancevariable1)
# obj.updatevariable(100)
# print(obj.instancevariable1)
# obj.r=0
# print(obj.r)