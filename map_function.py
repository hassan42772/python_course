numbers=["1","23","34"]
numbers=list(map(int,numbers))

numbers[2]=numbers[2]+2
print(numbers)

num=[2,3,4,5,6]

print(list(map(lambda x:x*x,num)))


def square(a):
    return a*a

def cube(a):
    return a*a*a
fun=[square,cube]

for i in range(5):
    vl=list(map(lambda x:x(i),fun))
    print(vl)