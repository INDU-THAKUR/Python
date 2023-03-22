text =input("enter the comment :")

if("make a lot of money" in text):
    spam=True
elif("buy now " in text):
    spam=True
elif("click this " in text):
    spam=True
elif("subscribe this " in text):
    spam=True   
else:
    spam=False
if(spam):
    print("text is spam")
else:
    print("This text is not spam") 