class Employee:
    company="google"    #-->class attributes 
    def getsalary(self): #--> class methods
        print(f"the salary of employee is {self.salary}")
    @staticmethod
    def greeting():
        print("good morning ,sir")


harry=Employee() #-->object instantiation
harry.salary=50000
harry.getsalary()
harry.greeting()