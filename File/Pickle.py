import pickle
# l=[1,5,7,6,4,5,7,5,4]
# f=open("this2.txt","wb")
# pickle.dump(l,f)

g=open("this2.txt","rb")
emp=pickle.load(g)
print(emp)