class Employee:
    def __init__(self,name,salary,subunit):
      self.name=name
      self.salary=salary
      self.subunit=subunit

    def printData(self):
        print(f"the name of employee is {self.name}")
        print(f"the salary of employee is {self.salary}")
        print(f"the ubunit of employee is {self.subunit}")

harry=Employee("harry",10000,"camera")
harry.printData()
