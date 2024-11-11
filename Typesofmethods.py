#There are 3 types of methods
#1.Instance method
#2.class method
#3.static method
#By default the methods we create in class are instance methods
#Instance methods are used to create/access/modify/delete the objects attributes
#Instance method performs operations on object attributes
#Creating instance methods:
# from types import MethodType
# class Employee:
#     A=10
#     def instancemethod(self):
#         print("instance method is nothing but a normal methods we create in class")
#     def __init__(self,a,b,c):
#         print("this is also the instance method")
#         self.a=a
#         self.b=b    #these insatance variables
#         self.c=c
#     def method2(self):
#         print(self.a) #access instance variable in instance method
#     def classvariable(self):
#         print(self.A)
#     def updatevariable(self,newvaribale):
#         self.A=newvaribale #changing class variable
#     def deleteinstancevariable(self):
#         del self.__class__.A
# emp=Employee(1,2,3) #object created
# emp.instancemethod() #instance method called
# print(emp.a)
# print(emp.b)
# print(emp.c)
# emp.method2()
# # print(emp.A)
# # emp.updatevariable(100)
# print(emp.A)
# emp.deleteinstancevariable()

# ####object.methodname=MethodType(func,object) to add method from outside
# def addingmethod(self):
#     print("method added successfully")
# emp.newinstancemethod= MethodType(addingmethod,emp)
# emp.newinstancemethod()
 #########################CLASS METHOD########################################
 #CLASS METHODS ARE USED TO MAKE OPERATIONS ON CLASS VARIABLES
 #WE CAN ACCESS CALSS METHODS USING CLASS AND ASLO WITH OBJECTS
 #why we create class method?
 #Ans:to perform operations on class level variables and to deal with factory methods
 #creating class method
 #syntax-->@classmethod
            # def methodname(cls,parameters):
            #     body
# class Student:
#     classvariable=100
#     @classmethod
#     def classmethod(cls):
#         print('classmethod')
#         print(cls.classvariable)
#         # cls.classvariable=101
#         del cls.classvariable


# Student.classmethod()
# student=Student()
# student.classmethod()
################################
# import datetime
# class student:
#     def __init__(self,name,id,age):
#         self.name=name
#         self.id=id
#         self.age=age
#     @classmethod
#     def getdob(cls,name,id,age):
#         return cls(name,id,datetime.datetime.now().year-age)
# stu=student.getdob('seshu',737,2001)
# print(stu.name,stu.id,stu.age)
#########STATIC METHOD###################
#static method is also called as utility function
#it's mostly used for general task
class calculator:
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def sub(a,b):
        return a-b
    @staticmethod
    def mul(a,b):
        return a*b
    @staticmethod
    def div(a,b):
        return a/b
c=calculator()
print(c.add(2,3))
print(c.sub(10,5))     