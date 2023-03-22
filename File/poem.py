f=open("poem.txt","r")
a=f.read()
if "twinkle" in a:
    print("twinkle is present\n")
else:
    print("twinkle is not present\n")
f.close()
print(a)