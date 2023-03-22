#-->operator overloading in Python
class Number:
    def __init__(self,num):  #-->constructure to initialize value to objects
        self.num=num
    
    def __mul__(self,num2):
        print("lets add")
        return self.num * num2.num

#creating objects
n1=Number(4)
n2=Number(6)
sum=n1*n2
print(sum)
