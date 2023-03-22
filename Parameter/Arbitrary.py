# def kids(*child):
#     print("the youngest child is",child[1])

# kids("akshay","ravi","rohit")

# def kids(child1,child2,child3):
#     print("the youngest child is",child1)

# kids(child1="akshay",child2="ravi",child3="rohit")

def kids(**child):
    print("the youngest child is",+ kids["child3"])

kids(child1="akshay",child2="ravi",child3="rajesh")
