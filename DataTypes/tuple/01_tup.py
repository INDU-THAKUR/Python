# Python Tuples are like a list. It can hold a sequence of items. 
# The difference is that it is immutabable
b= 1, 2.0, 'three'
print(type(b))  # tuple packing also declare tuple
print(b)


t=(1,4,6,"a",5)
t1=()  #-->empty tuple
print(t1) 

t2=(1) #--> wrong way to declare tuple with one element
print(t2)

t3=(1,)  #-->tuple with one element
print(t3)

#->once defined a tuple elements cannot be altered or changed
print(type(t))
print(t)

# t[0]=32  #-> throw an error because we can't alter 
           # elements of tuple after creation