class employee:
    company="google"
    
    def content(self):
        print("Google is a good company")

class programmer:
    company="youtube"
    
    def content(self):
        print("youtube is a good company")

class freelancer(programmer,employee):
    name="Ravi"

    def showname(self):
        print(f"The name of the freelancer is {self.name}")

f=freelancer()
f.showname()
f.content()
print(f.company)