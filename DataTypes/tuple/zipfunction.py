''' 1.The zip() function returns a zip object, which is an iterator of tuples 
 where the first item in each passed iterator is paired together, 
then the second item in each passed iterator are paired together
then third item in each passed iterator are paired together and so on'''

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)
print(x)

''' 2.If the passed iterators have different lengths, the iterator with the 
least items decides the length of the new iterator.'''

c = ("John", "Charles", "Mike")
d = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(d, c)
print(tuple(x))

