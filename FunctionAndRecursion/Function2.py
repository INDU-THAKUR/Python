#->a function in python is a block of code which execute only when it is called
#--> you can pass data known as parameter into an function
#--> a function can return data in return


# creating a function in python

def sum(a,b,c):
      return a+b+c
    
d=int(input("enter your first number: "))
e=int(input("enter your second number: "))
f=int(input("enter your third number: "))

h=sum(d,e,f)
print(h)

#--> in above expression a,b,c-->parameters and d,e,f-->arguments

#--> by default ,a function must be called with the correct 
# number of arguments,neither more nor less 

#-->meaning if we called the above function by specifing 
# only two or four argument it will throw an error
