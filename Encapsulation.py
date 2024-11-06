#Encapsulation-->combining related things in to a single unit
#Advantages-->code will be organised and clean
        #  -->prevents the data from accidental removal and deletion
#Wrapping data and methods in to a single unit
# Datahiding+Abstraction=Encapsulation
#Hides implementation logic and allows only to use
#ACCESS MODIFIERS 
#       |
#public access specifiers
#protected access specifiers
#private access specifiers
#Let's see public access specifiers or public access modifiers or public memeber
#                           |
#   any where in the class we can use when we declare in public member
# if data declare in public access we can access date 
#-->in same class
#-->by object
#--we can access from subclass & access by subclass object
#let's see with example
# class parent:
#     publicdata=10
#     def publicmethod(self):
#         print(self.publicdata)
# class child(parent):
#     def method(self):
#         print(self.publicdata)
# obj1=parent()
# obj1.publicmethod()
# print(obj1.publicdata)
# obj2=child()
# obj2.publicmethod()
# print(obj2.publicdata)
# --------------------------------------------
#2.protected acccess specifier
#--> if data declare in protected it can access only that class and derived class
#put _ before data & method to declare as protected
# class parent:
#     _protecteddata=10
#     def protected(self):
#         print(self._protecteddata)
# class child(parent):
#     def method(self):
#         print(self._protecteddata)
# obj1=parent()
# obj1.protected()
# obj2=child()
# obj2.method()
# print(obj2._protecteddata)

#3.private access specifier
#-->put __ before data & method to declare as private
# class parent:
#     __privatedata=10
#     def private(self):
#         print(self.__privatedata)
# class child(parent):
#     def method(self):
#         print(self.__privatedata)
# obj1=parent()
# obj1.private()
# print(obj1._parent__privatedata)

##### to access the private access specifies here comes the namemagling concept#######
#Namemangling-declare data or method with atleast 2 leading underscores and atmost 1 trailing underscore.
#then it will replace to __classNameName by the interpreter
###############DATA HIDING#####################################################################
#Datahiding-->declare data in one class, doesn't give access to another class and hides the data
#to give security to sensitive information
################ABSTRACTION AND ABSTRACT CLASS###################################################
#the process of handling complexity by hiding unnecessary information from user is called abstraction
#we can implement abstraction using abstract class
#If a class contain one or more than one abstract method then the class is called abstract class
#if the method is declared without implementation it is called abstract method
############let's see basic example#######################
# from abc import ABC,abstractmethod
# class A(ABC):
#     @abstractmethod
#     def method1(self):
#         pass
#     def method2(self):
#         print("Iam a concrete method")
#     @abstractmethod
#     def method3(self):
#         pass
# class B(A):
#     def method1(self):
#         print("method1 implemented in subclass")
#     def method3(self):
#         print("method3 implemented in subclass")
# obj=B()
# obj.method1()
# obj.method2()
# obj.method3()
##################POLYGON EXAMPLE########################3
# from abc import ABC,abstractmethod
# from math import sqrt
# class Polygon(ABC):
#     @abstractmethod
#     def sides(self):
#         pass
#     @abstractmethod
#     def Area(self):
#         pass
#     @abstractmethod
#     def Perimeter(self):
#         pass
#     def figure(self):
#         return 'it is a 2-dimensional plane figure'
# class rectangle(Polygon):
#     def sides(self,l,b):
#         self.l=l
#         self.b=b
#     def Area(self):
#         return self.l*self.b
#     def Perimeter(self):
#         return 2*(self.l+self.b)
#     def extramethod(self):
#         return 'rectangle has 4 sides'
# class Triangle(Polygon):
#     def sides(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#     def Area(self):
#         s=self.Perimeter()
#         return sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
#     def Perimeter(self):
#         return (self.a+self.b+self.c)/2
#     def extramethod(self):
#         return 'triangle has 3 sides'
# class Square(Polygon):
#     def sides(self,side):
#         self.side=side
#     def Area(self):
#         return self.side*self.side
#     def Perimeter(self):
#         return 4*(self.side)
#     def extramethod(self):
#         return 'square has 4 sides'
# r=rectangle()
# r.sides(10,20)
# t=Triangle()
# t.sides(2,4,6)
# s=Square()
# s.sides(10)
# for obj in [r,t,s]:
#     print(obj.Area())
#     print(obj.Perimeter())
    
