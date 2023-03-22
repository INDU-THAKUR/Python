def factorial(b):
    if(b==0 or b==1):
        return 1
    else:
        return b*factorial(b-1)

z=int(input("enter the number:"))
print(factorial(z))
     