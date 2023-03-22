# class Number:
#      def sum(self):
#          return self.a +self.b

# num=Number() #->creating object
# num.a=4
# num.b=8
# s=num.sum()
# print(s)

class RailwayForm:
    formType="RailwayForm"
    def printData(self):  #-->class method
        print(f"Name is {self.name}")
        print(f"Name is {self.train}")

harrysApplication =RailwayForm() #->creation of object
harrysApplication.name="harry"  #-->giving values to class attributes
harrysApplication.train="Rajdhani Express"
harrysApplication.printData() #--> calling a class function