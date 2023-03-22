a=int(input("enter number a :"))
b=int(input("enter number b :"))
c=int(input("enter number c :"))
d=int(input("enter number d :"))
if(a>d):
    f1=a
else:
    f1=d

if(b>c):
    f2=b
else:
    f2=c

if(f1>f2):
    print(str(f1) + "is greatest")
else:
    print(str(f2) + "is greatest")