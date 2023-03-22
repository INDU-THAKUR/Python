#1.add-->Adds an element to the set
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

#2.clear-->Removes all the elements from the set
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

#3.copy  -->Returns a copy of the set
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

#4.difference  -->return a new set
# Returns a set containing the difference between two or more sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y) #-->print those elements of x that are noy=t in y
print(z)

#5.difference update -->return an updated set
#Removes the items in this set that are also included in another,
#  specified set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

#6.discard -->Remove the specified item
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

#7.intersection  --> returns a new set,without the unwanted value
# Returns a set, that is the intersection of two or more sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#8.intersection update -->removes unwanted value from original set
#Removes the items in this set that are not present in other, specified set(s)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#9.isdisjoint -->Returns whether two sets have a intersection or not
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)
 
#10.issubset  -->Returns whether another set contains this set or not
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

#11.issuperset -->Returns whether this set contains another set or not
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

#12.pop -->Removes an random element from the set
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

#13.remove -->Removes the specified element
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

#14.symmetric difference -->
# Returns a set with the symmetric differences of two sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

#14.symmetriv difference update-->
# inserts the symmetric differences from this set and another
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#15.union-->	Return a set containing the union of sets
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.union(y)
# print(z)

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z)
print(result)

#16.update -->Update the set with another set, or any other iterable
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)

