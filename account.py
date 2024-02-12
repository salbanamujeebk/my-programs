d={}
def create():
    a=int(input("enter the number of pairs: "))
    for i in range (a):
        p=input("enter your a/c No: ")
        if p not in d:
            q=int(input("enter your savings: "))
            d[p]=q
        else:
            print("account already exist.")
    print(d)
def deposite():
    p=input("enter the a/c No: ")
    if p in d:
        q=int(input("enter the amount: "))
        d[p]+=q    
        print("{} deposited to account {}.Your current balance is: {}".format(q,p,d[p]))
    else:
        print("account does not exist")
def withdrawal():
    p=input("enter the a/c No: ")
    if p in d:
        q=int(input("enter the amount: "))
        if d[p]>=q:
            d[p]-=q
            print("{} withdraw from the account{}. Your current balance is: {}".format(q,p,d[p]))
        else:
            print("No balance exist")
    else:
        print("account does not exist")
    
while True:
    print("1: creation "
            "\n2: deposite"
            "\n3: withdrawal"
            "\n4: display"
            "\n5: Exit")
    x=int(input("enter your choice"))
    if x==1:
        create()
    elif x==2:
        deposite()
    elif x==3:
        withdrawal()
    elif x==4:
        print(d)
    elif x==5:
        break