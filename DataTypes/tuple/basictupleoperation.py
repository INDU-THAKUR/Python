#1.Adding an element to tuple
t = (1, 2, 3, 4, 5)
# t = t + (7,)
# print (t)

#2.adding two tuples
print ((1, 2, 5, 8) + (2, 9, 4))

# 3.delete tuple
t = (1, 2, 3, 4, 5)
del(t)
print(t)

#4.slicing
print(t[2:4]) #->index 2 to 3

#5.multiplication
print (t*3)

#6.In
t1= (1, 2, 3, 6, 7, 8)
print(2 in t1)
print(5 in t1)

#7.len
print(len(t1))

#8.compare  --> not working in python 3.x
t1= ((1, 2, 3, 6, 7, 8) > (1, 2, 3, 4, 5, 7))
print(t1)

#9.max and min
t3= (1, 4, 2, 7, 3, 9)
print (max(t3))
print (min(t3))

#10. converting a list into tuple
l= [1, 4, 2, 7, 3, 9]
print(tuple(l))

#11.sorting
g=(1,4,2,6,8,3,9,4,5,7,0,5,6,9,4,8)
print(sorted(g))   #-->sort can be used only in list class

#12. arithmatic sum
print(sum(g))