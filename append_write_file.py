# write function
f=open("hassan.txt","w")
f.write("hassan cgpa is very good")
print(f)
# append function
f=open("hassan.txt","a")
f.write("hassan cgpa is very good \n hassan stood first in class")
print(f)
# r+ function
f=open("hassan2.txt","r+")
print(f.read())
f.write("hassan is a pubg player \n")
print(f)
