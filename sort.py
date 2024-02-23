a=[]
b=int(input("enter the number: "))
for i in range(b):
    c=int(input("enter the number: "))
    a.append(c)
    a.sort()
    print(a)
    x=(len(a))
y=x//2
p=a[:y]
q=a[y:]
q.reverse()
print(p+q)
