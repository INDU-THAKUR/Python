# x=3
# try:
#     print(x)
# except NameError:
#     print("this is a nameerror")
# except:
#     print("this is exception")
# else:
#     print("everything is OK")
# # finally:
#     print("this is printing regardless the output of try and excepy block")

# x=-1
# if x<0:
#     raise Exception("no number below 0 is allowed")

x="hello"
if type(x) is not int:
    raise TypeError("it is an TypeError")