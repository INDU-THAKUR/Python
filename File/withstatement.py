with open("write.txt","r") as f:
    a=f.read()  #--> no need to use f.close()
# with open("write.txt","w") as f:
#     f.write("this in me using with functions")    
print(a)
