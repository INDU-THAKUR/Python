class person:
    country="india"

    def takebreath(self):
        print("i am breathing")

class employee(person):
    company="honda"

    def getsalary(self):
        print("the salary of the employee is 60K ")

class programmer(employee):
    company="maruti"
    name="akshay"

    def getname(self):
        print(f"the name of programmer is {self.name}")
    def getsalary(self):
        print("no salary to programmer ")

p=programmer()
p.takebreath() #-->execute takebreath of person class
p.getsalary()
p.getname()

    