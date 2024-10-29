#CLASS SYNTAX
#class ClassName:
    # statement 1
    # statement 1
    # statement 1
    # statement 1
        #    :
        #    :
        #    :
    #statement n
#----------------------------------------------------------------------------------------------------
#class example:
# class SampleClass:
#     pass            ---> this is basic class syntax here we haven't seen any attributes or methods
#-----------------------------------------------------------------------------------------------------
#---> now lets see by adding attributes
# class SampleClass:
#     attribute1=10
#     attribute2=20     #--->these are the attributes 
# # if we need to access the attributes we need to use-->className.attributes/className.methods
# print(SampleClass.attribute1)
# print(SampleClass.attribute2)
#----------------------------------------------------------------------------------------------------
# NOW LET'S SEE OBJECT CREATION
# class SampleClass:
#     attribute1=10
#     attribute2=20
# # to create object we need to create object and need to assign-->object=ClassName()
# object1=SampleClass()
# object2=SampleClass()
# print(object1.attribute1)
# print(object2.attribute2)
#-----------------------------------------------------------------------------------------------------
#NOW LET'S AFTER CREATING OBJECT HOW CAN WE CHANGE THE ATTRIBUTES FOR OBJECTS
# class SampleClass:
#     attribute1=10
#     attribute2=20
# obj1=SampleClass()
# obj2=SampleClass()
# obj3=SampleClass()
# # now to change attribute for object or to modify the attributes of class for this object-->obj.attribute=''
# obj1.attribute1=100
# print(obj1.attribute1)
#---------------------------------------------------------------------------------------------------------------
#NOW LET'S SEE HOW TO CREATE METHODS 
# class SampleClass:
#     def SampleMethod(self):     #--> syntax for method creation self should be there as a default parameter
#         print(" this is sample method")
# obj1=SampleClass()
# obj1.SampleMethod()
#--------------------------------------------------------------------------------------------------------------
# NOW LET'S THE __INIT__ () METHOD
# __init__() method if we create this method in class it will automatically get's executed when we call the class
# what's the use of this method is when we need to store attributes intially in object then these attribute will be created in init method
#this method nothing but a constructor in OOPS
        #Synatx for INIT METHOD
# def __init__(self,parameter1,parameter2...,parametern):
#     self.parameter1=parameter1
#     self.parameter2=parameter2
#                :
#                :
#     self.parametern=parametern
            #let's see example
# class SampleClass:
#     def __init__(self):
#         print("this method automatically get's called when class was created")
# obj1=SampleClass()
            #let's the another example with bankaccount example
class BankAccount:
    def __init__(self,accountno,accountname,ifsccode,balance):
        self.accountno=accountno
        self.accountname=accountname
        self.ifsccode=ifsccode
        self.balance=balance
    def display(self):
        print(self.accountno,self.accountname,self.ifsccode,self.balance)
obj1=BankAccount(7013979055,'Seshu','hdfc0007',100000)
obj1.display()
        
