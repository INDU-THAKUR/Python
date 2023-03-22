#1.The frozenset() is an inbuilt function in Python which takes an iterable object as input and makes them immutable. 
#.Simply it freezes the iterable objects and makes them unchangeable

#2.frozenset is the same as set except the forzensets are immutable
#  which means that elements from the frozenset cannot be 
# added or removed once created.

#3.Syntax : frozenset(iterable_object_name)
#Parameter : This function accepts iterable object as input parameter.
#Return Type: This function return an equivalent frozenset object

# Python program to understand frozenset() function
 
# tuple of numbers
t = (1, 2, 3, 4, 5, 6, 7, 8, 9)
 
# converting tuple to frozenset
fnum = frozenset(t)
 
# printing details
print("frozenset Object is : ", fnum)



# Python program to understand
# use of frozenset function
 
# creating a list
favsub= ["OS", "DBMS", "Algo"]
 
# making it frozenset type
fsub = frozenset(favsub)
 
# below line will generate error
 
favsub[1] = "Networking"
print(favsub)

# fsub[1]="networking" #-->frozen set does not allow element assignment




# Python program to understand use
# of frozenset function
 
# creating a dictionary
Student = {"name": "Ankit", "age": 21, "sex": "Male",
           "college": "MNNIT Allahabad", "address": "Allahabad"}
 
# making keys of dictionary as frozenset
f= frozenset(Student)
 
# printing keys details
print('The frozen set is:', f)