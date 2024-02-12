d={}
def create():
    a=int(input("enter the number of pairs; "))
    for i in range (a):
        p=input("enter the key: ")
        q=input("enter the value: ")
        d[p]=q
    print("created")
def update():
    p=input("enter the key: ")
    if p in d:
        q=input("enter the value: ")
        d[p]=q
    else:
        print("invalid")   
def delete():
    p=input("enter the key: ")
    if p in d:
        d.pop(p)

def display():
    print(d)
while True:
    print("1: creation "
          "\n2: update"
          "\n3: delete"
          "\n4: display"
          "\n5: Exit")
    x=int(input("enter your choice"))
    if x==1:
        create()
    elif x==2:
       update()
    elif x==3:
       delete()
    elif x==4:
        print(d)
    elif x==5:
        break