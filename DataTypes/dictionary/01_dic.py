# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*,---> in python 3.7 dictionary are ordered
#  changeable and does not allow duplicates


myDict = {
    "Fast":"in a quick manner",
    "akshay":"a coder",
    "marks":[23,56,78],
    "anotherDict":{"harry":"player"}
}
print(type(myDict))
print(myDict["Fast"])
print(myDict["akshay"])
print(myDict["marks"])  
myDict['marks']=[23,56]   #-->mutable,contain no duplicate value
print(myDict["marks"])
print(myDict["anotherDict"])