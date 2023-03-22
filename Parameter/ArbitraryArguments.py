#--> Arbitrary arguments are often shortend to *args in python
#-->if you dont know the exact number of arguments that will passed into
# your function,add a * before the parameter name in function definition

# --> this way the function will receive a tuple of arguments,
# and access item accordingly

def my_function(*kids):
  print("The youngest child is " + kids[1])

my_function("Emil", "Tobias", "Linus")






