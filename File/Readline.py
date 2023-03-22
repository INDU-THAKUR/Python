f= open('this.txt')
# data=f.read()

#read first line
data=f.readline() 

#read second line
print(data)  

#.....so on
data=f.readline() 
print(data)   

f.close() 