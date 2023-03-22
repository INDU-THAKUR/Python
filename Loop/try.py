# #1.
# try:
#   print(x)
# except:
#   print("An exception occurred")


#2. with multiple except
# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")

# 3. with else
# try:
#   print("hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

#4.with finally
# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")

#5.To throw (or raise) an exception, use the raise keyword
# x = -1

# if x < 0:
#   raise Exception("Sorry, no numbers below zero")


x = "hello"

if  type(x) is not int:
  raise TypeError("Only integers are allowed")