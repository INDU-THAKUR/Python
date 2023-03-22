# def percentage(marks):
#     p=((marks[0]+marks[1]+marks[2]+marks[3])/4)
#     return p

# marks1=[45,56,75,76]
# percentage1=percentage(marks1)
# marks2=[34,56,65,76]
# percentage2=[23,34,56,45]
# percentage2=percentage(marks2)
# print(percentage1,percentage2)

# c=[23,56,87,98]
# d=sum(c)  #--> built in function
# print(d)

# def sum(a,b):
#     return a+b

# c=23
# d=45
# print(sum(c,d))

def greatest(a,b,c):
    if(a>b):
        print("a is greater and the value of a is",a)
    elif(b>c):
        print("b is greater and the value of b is",b)
    else:
        print("c is greater and the value of c is",c)

d=75
e=45
f=56
f=greatest(d,e,f)
print(f)