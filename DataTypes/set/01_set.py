#1.Sets are used to store multiple items in a single variable.

#2.Set is one of 4 built-in data types in Python used to store
# collections of data, the other 3 are List, Tuple, 
#and Dictionary, all with different qualities and usage

#3.Sets are written with curly brackets

#4.A set is a collection which is both unordered and unindexed

#5.Once a set is created, you cannot change its items,
#  but you can add new items

#6.Sets cannot have two items with the same value

#7.A set can contain different data types

#8.There is no index attached to any element in a python set.
#  So they do not support any indexing or slicing operation

a={1,2,45,2,4,"banana",5,4,True,56}
print(a)
print(type(a))

#-> empty set
b={} #-->worng way,print dictionary
print(type(b))

c=set() #set()->set constructor 
print(type(c))
c.add(4)
c.add(5)
# c.add([3,5,4]) -->you can,t add list to the set because it is unhashable
c.add((3,2,8,4)) #-->you can add tuple
# c.add({4:5}) you also cant add dict to set because it is also unhashable
print(c)

#. creating set using set constructor

d=set((1,4,7,2,'banana',45))  # note the double round-brackets
print(d)

#. len function
print(len(d))

#.remove functiom
# d.remove(4,7) #.doesn,t work wit two or more arguments
d.remove(4)
print(d)