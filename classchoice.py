class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        ar=3.14*self.radius**2
        print("Area of your circle is: ",ar)
        cir=2*3.14*self.radius
        print("Circumference of your circle is: ",cir)
class person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def display(self):
        print(self.name)
        print(self.age)
        print(self.address)
class book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def library(self):
        print(self.title)
        print(self.author)
        print(self.price)



while True:
    print("1.Calculate circle\n"
          "2.Display person Details\n "
          "3.Display Book Info\n"
          "4.Exit")
    a=int(input("Enter Your Choice: "))
    if a==4:
        break
    elif a==1:
        radius=int(input("Enter the radius of circle: "))
        q=circle(radius)
        q.area()
    elif a==2: 
        name=input("enter the person's name : ")
        age=int(input("enter person's age : "))
        address=(input("enter person's address : "))
        q=person(name,age,address)
        q.display()
    elif a==3:
        title=input("Enter the title of the Book: ")
        author=input("Enter the name of author: ")
        price=int(input("enter the price of the book: "))
        q=book(title,author,price)
        q.library()