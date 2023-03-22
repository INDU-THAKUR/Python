class Employee:
    company="google"
    def showdetails(self):
        print(f"this is an employee")

class Programmer(Employee):  #-->means programmer is inherited from employee class
    language="python"
    def getdetails(self):
        print("this is a programemr")

akshay= Programmer()  #-->create object of programmer class
akshay.showdetails()
akshay.getdetails()  #-->object of derived class use method of base class
print(akshay.company)
print(akshay.language) #-->object of derived class use attributes of base class