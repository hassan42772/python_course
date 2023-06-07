# rt is default
f=open("hassan.txt","rt")
content=f.read()
print(content)
# for  read character by charater
for line in content:
    print(line)
# to read line by line
for line in f:
    print(line,end="")
# readline() function
print(f.readline())
print(f.readline())
print(f.readline())
# readlines( ) function
print(f.readlines())
f.close()