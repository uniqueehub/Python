a=input("Number: ")
a=int(a)
if(a%2==0):
    print("Even")
else:
    print("Odd")
e=["hejn","hfj"]
b=["pasta","pizza"]
c=["noddles","yamin"]
d=input("Enter dish: ")
if d in b:
    print("B")
elif d in c:
    print("C")
elif d in e:
    print("E")
else:
    print("no")