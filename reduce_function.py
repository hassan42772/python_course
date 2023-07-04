from functools import reduce

list1 = [1,2,3,4,2]
num = reduce(lambda x:x, list1)
# num = 0
# for i in list1:
#     num = num + i
print(num)