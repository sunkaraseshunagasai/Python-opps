# if the class contains more than one method has same name
#and the method contains different datatypes of parameters or different no of parameters or both is called method overloading
#features of method overloading
#-->flexiblity,readability
#python doesn't support method overloading because it's dynamically typed language
#if we want to use method overloading we need to install module multipledispatch
# import multipledispatch
# class A:
#     @multipledispatch.dispatch(int,int)
#     def add(self,a,b):
#         return a+b
#     @multipledispatch.dispatch(int,int,int)
#     def add(self,a,b,c):
#         return a+b+c
#     @multipledispatch.dispatch(str,str)
#     def add(self,a,b):
#         return a+b
# obj=A()
# print(obj.add(1,2))
# print(obj.add(1,2,3))
# print(obj.add('seshu','sai'))
#--------------------------------
# class A:
#     def add(self,*args):
#         if args:
#             s=type(args[0])()
#             for i in args:
#                 s=s+i
#             return s
# obj=A()
# print(obj.add(1,2,3,4))
# print(obj.add('seshu','sai'))
