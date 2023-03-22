l1=[1,5,3,7,4,5,2,9,35,5,32]
print(l1)
l1.sort() #-> sort the list
print(l1)

l1.reverse() #->reverse the list
print(l1)

# l1.append(5)  #-> adds at the end of the list
# l1.append(8) 
# print(l1)

# l1.insert(5,10)  #-> insert 10 at index 5
# print(l1)

# l1.pop(2)  #-> will delete element at index 2 and return its value
# print(l1)

# l1.remove(32)  #-> will remove 32 from list
# print(l1)

# l1.extend([3,23,443,56,2]) #--> extend the list
# print(l1)

# l1.clear() #--> clear all elements fron list
# print(l1)

print(l1.index(32))  #--> give the index position of element

print(l1.count(5))   #-->give the count of an element

# WITHOUT copy()
# a = ["bee", "wasp", "moth"]
# b = a
# b.append("ant")
# print(a)
# print(b)

# # WITH copy()
# a = ["bee", "wasp", "moth"]
# b = a.copy()
# b.append("ant")
# print(a)
# print(b)