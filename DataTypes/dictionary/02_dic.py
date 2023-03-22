#1. clear
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)
car.clear()
print(car)

#2.copy
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.copy()
print(x)

#3.fromskey  #-->create dictionary from tuples
x = ('key1', 'key2', 'key3')
y = 0
print(type(x))
thisdict = dict.fromkeys(x, y)
print(thisdict)

#4.get  -->The get() method returns the value of the 
car = {               #item with the specified key.
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x)

#5.items -->The view object contains the key-value pairs
               #  of the dictionary, as tuples in a list
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x)

#6.keys -->The view object contains the keys of the dictionary, as a list.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x)

#6a.values  -->The values() method returns a view object
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)

#7.pop -->The pop() method removes the specified item from the dictionary.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)

#8.popitem -->The popitem() method removes the 
             #  item that was last inserted into the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem()
print(car)

#9.setdefault  Returns the value of the specified key.
    #  If the key does not exist: insert the key, with the specified value
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)

#another example
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("color", "White")
print(car)
print(x)

#10.update  -->Updates the dictionary with the specified key-value pairs
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"tyre": "six"})
print(car)