class Employee():
    company="google"  #->class attributes
    salary=100
harry=Employee() #--> object instantiation
rajni=Employee()
harry.salary=120
print(harry.company)
print(rajni.company)
print(harry.salary)
print(rajni.salary)