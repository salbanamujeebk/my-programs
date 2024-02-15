def circle():
    a=int(input("enter the radius : "))
    perimeter=2*3.14*a
    print("perimeter of a circle is: ",perimeter)
def square():
    b=int(input("enter the length of a side"))
    perimeter=4*b
    print("perimeter of the square is : ",perimeter)
def book():       
    d={}
    def create():
        a=int(input("enter the number of pairs; "))
        for i in range (a):
            p=int(input("enter the number: "))
            q=input("enter the book name: ")
            d[p]=q
        print("created")
    def display():
            print(d)        
    def delete():
        p=input("enter the key: ")
        if p in d:
            d.pop(p)

    def edit():
        p=int(input("enter the number: "))
        q=input("enter the book name: ")
        if p in d:
            d[p]=q
    while True:
        print("1: create "
            "\n2: display"
            "\n3: delete"
            "\n4: edit"
            "\n5: Exit")
        x=int(input("enter your choice"))
        if x==1:
            create()
        elif x==2:
            display()
        elif x==3:
            delete()
        elif x==4:
            edit()
        elif x==5:
            break
            
while True:
    print("1: circle perimeter "
        "\n2: square perimeter"
        "\n3: book"
        "\n4: exit")
    x=int(input("enter your choice"))
    if x==1:
        circle()
    elif x==2:
        square()
    elif x==3:
        book()
    elif x==4:
        break
