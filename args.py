def names(a,b):
    print(a,b ,"are good boys")
names("ali","ahamd")
# args
def lists_of_students(*lis):
    for item in lis:
        print(item)
listies=["ali","ahamd","bilal","zaryab"]
lists_of_students(*listies) 
# normal
def lists_of_students(normal,*lis):
    print(normal)
    for item in lis:
        print(item)
normal="all students are intelligent"
listies=["ali","ahamd","bilal","zaryab"]
lists_of_students(normal,*listies) 
# **kwargs
def lists_of_students(normal,*lis,**kwargs):
    print(normal)
    for item in lis:
        print(item)
    for i ,j in kwargs.items():
        print(f"{i} is key and{j} is value")


normal="all students are intelligent"
listies=["ali","ahamd","bilal","zaryab"]
ke={"ali":"apple","hassan":"pizza","anas":"burger"}
lists_of_students(normal,*listies,**ke) 