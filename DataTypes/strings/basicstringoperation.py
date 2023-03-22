#1.concatenate
a = "Tea " + "Leaf"
print(a)

#2.repeate the string to specified number of times 
a = "Bee " * 3
print(a)

#3.slice
a = "Sea"
print(a[1])

#4.range slice
a = "Mushroom"
print(a[4:8])

#5.in
a = "Mushroom"
print("m" in a)
print("b" in a)
print("shroo" in a)

#6.not in
a = "Mushroom"
print("m" not in a)
print("b" not in a)
print("shroo" not in a)

#7.r
a = "1" + "\t" + "Bee"  #-->it prevents the escape character 
b = "2" + r"\t" + "Tea"  # from being an escape character.
print(a)
print(b)


#8.%  -->Performs string formatting
a = "Hi %s" % ("Homer")
print(a)