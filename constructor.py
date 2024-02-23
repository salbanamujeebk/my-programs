# ------->default constructor<-------

# class Employee:
#     a=int(input("enter your Id: "))
#     b=input("enter your name: ")
#     c=int(input("enter the phone number: "))
#     d=int(input("enter your salary: "))
#     def show(self):
#         print(self.a,self.b,self.c,self.d)
# employee=Employee()
# employee.show()


# -----=>parameterised costructor<------



# class Employee:

#     def __init__(self,a,b,c,d):
#         self.a=a
#         self.b=b
#         self.c=c
#         self.d=d
#     def display(self):
#         print(self.a,self.b,self.c,self.d)
# a=int(input("enter your Id: "))
# b=input("enter your name: ")
# c=int(input("enter the phone number: "))
# d=int(input("enter your salary: ")) 
# q=Employee(a,b,c,d) 
# q.display() 



# ---->nonparameterised constructor<-------

class Employee:
    def display(self,a,b,c,d):
        print(a,b,c,d)
a=int(input("enter your Id: "))
b=input("enter your name: ")
c=int(input("enter the phone number: "))
d=int(input("enter your salary: "))
q=Employee()
q.display(a,b,c,d)