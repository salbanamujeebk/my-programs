
a=[]
def add():
    n=int(input("enter how many pairs: "))
    for i in range(n):
        b=[]  
        name=input("enter your vehicle :")
    
        if name in b:
            print(f"{name} already exisist")
        else:
            price=int(input("enter your v-price:"))
            wheel=int(input("how many wheel:"))
            b.append(name)
            b.append(price)
            b.append(wheel)
            a.append(b)
            print(b)  
            print(a) 
def  display():
    def two():
        for j in a:
            if j[2]==2:
                print(f"{j[0]} - Price: {j[1]}")
           
    def three():    
       
        for j in a:
            if j[2]==3:
                print(f"{j[0]} - Price: {j[1]}")
            
    def four():    
       
        for j in a:
             if j[2]==4:
                print(f"{j[0]} - Price: {j[1]}")
                
    while True:
            print(  "1:two-wheel  \n"
                    "2:three-wheel\n"
                    "3:four-wheel\n"
                    "4:exit\n") 
            y=int(input("enter your choice: "))
            if y==4:
                break
            elif y==1:
                two()
            elif y==2:
                three()    
            elif y==3:
                four()                   
while True:
    print(
    "1:Add  \n"
    "2:Display\n"
    "3:exit\n") 
    y=int(input("enter your choice: "))
    if y==4:
        break
    elif y==1:
        add()
    elif y==2:
        display()