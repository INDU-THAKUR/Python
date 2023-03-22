# try:
#     print(x)
# except:
#     print("an error has occured")

# try:
#     print(x)
# except NameError:
#     print("a name error has occured")
# except:
#     print("something else went wrong")

# try:
#     print(x)
# except:
#     print("an error has occured")
# else:
#     print("nothing went wrong")

# try:
#     print(x)
# except:
#     print("an error has occured")
# finally:
#     print("this is print regardeless the output of output of try and except statement")

#-->raise keyword is used to throw an error
# x=int(input("enter any number: "))
# if x<0:
#     raise Exception("the number is negative")
# print(x)


a="hello"
if type(a) is not int:
    raise TypeError("invalid input type")

