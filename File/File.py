# File Methods
# #1.open
# f=open("this.txt","r")

#2.read
# data=f.read()
# print(data)
# data=f.read(2) #-->read only two characters

#2a.readline-->if we have 4 lines we have to call it 4 times
# data=f.readline()
# print(data)
# data=f.readline()
# print(data)
# data=f.readline()
# print(data)
# data=f.readline()
# print(data)

#2b.readlines --> give a list of lines
# data=f.readlines()
# print(data)

#3.seek
# f.seek(7)

# #4.tell
# print(f.tell())

#5.write
# f=open("this2.txt","w")
# f.write("this is my first program")

#5a.writelines
# f = open("this2.txt", "a")
# f.writelines(["\nSee you soon!", "\nOver and out."])
# f.close()

#6
# f = open("this2.txt", "r+")
# print(f.readable())
# print(f.writable())

#7.rename
# import os
# os.rename("this.txt","renamed file")

#8.remove
# import os
# os.remove("renamed file")


# file attributes
# f=open("this2.txt","r")
# print("the name of the file is ",f.name)
# print("the mode of the file is", f.mode)
# print("the encoding of the file is", f.encoding)
# print("is file closed ",f.closed)

#pickle module-->used to serializing and  deserializing a 
# python object moduel
#2.Any object on python is pickled so that it can be saved on disk
#3.pickle is a method to convert a python object into character stream

import pickle
l=[1,5,7,6,4,5,7,5,4]
f=open("this2.txt","wb")
pickle.dump(l,f)

g=open("this2.txt","rb")
emp=pickle.load(g)
print(emp)