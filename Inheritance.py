                                #INHERITANCE
#Inheritance is nothing but a ability to use methods and attributes in newly
#created class from already creted class.
#creating a new class from already created class
# for example if we inherit properites and mehtods from another class that  class
#be known as derived class or child class or subclass and the class from where we are 
#inheriting is known as superclass or base class or parentclass
#There are five types of inheritances
#1.Single inheritance
# 2.Multiple inheritance
# 3.Multilevel inheritance
# 4.Hierarchical inheritance
# 5.Hybrid inheritance
# ---------------------------SINGLE INHERITANCE------------------------------------
# Let's see an example
# class Parent():
#     def method1(self):
#         print("I'm from parent class")
# class Child(Parent):
#     def method2(self):
#         print("I'm from child class")
# parent=Parent()
# child1=Child()
# child1.method2()
# child1.method1()
# parent.method1()
# --------------------------MULTIPLE INHERITANCE----------------------------------------
#IF CHILD CLASS INHERITS FROM MORE THAN ONE PARENT CLASS THEN IT'S A MULTIPLEINHERITANCE
# class Father():
#     def method1(Self):
#         print("I'M a father")
# class Mother():
#     def method2(self):
#         print("i'M A MOTHER")
# class Child(Father,Mother):
#     def method3(self):
#         print("I'm a child class")
# child1=Child()
# child1.method1()
# child1.method2()
# child1.method3()
#-----------------------MULTILEVEL INHERITANCE---------------------------------------------
#grandparent-->parent->child---here parent inherits from grandparent and child inherits from parent
# class Grandparent:
#     def method1(self):
#         print("i'm tattayya")
# class Parent(Grandparent):
#     def method2(self):
#         print('nenu ra nanna nii')
# class Child(Parent):
#     def method3(self):
#         print("daddy nenu nii kodukuni")
# child=Child()
# print(Child.__mro__)
# child.method1()
# ------------------------Heirrarical inheritance------------------------------------------------------------
#Parent class-->childclass1
#            |-->childclass2
# class parent:
#     def method1(self):
#         print("iam parent class")
# class child1(parent):
#     def method(self):
#         print("nen pedda kodukuni")
# class child2(parent):
#     def method(self):
#         print("nen chinna kodukuni")
# c1=child1()
# c2=child2()
# c1.method()
# c1.method1()
# c2.method()
# c2.method1()
#-----------------------HYBRID INHERITANCE-------------------------------------------------
# combination of more than one inheritance is called hybrid inheritance
class Grandparent:
    def method1(self):
        print("grandparent")
class Father(Grandparent):
    def method2(self):
        print("iam father")
class Mother:
    print("iam mother")
class Child(Father,Mother):
    print("iam child")
child=Child()
child.method1()
child.method2()
print(Child.__mro__)
        