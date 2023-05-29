list1=["hassan","ahmad","bilal","ali"]
for item in list1:
    print(list1)

name={
    "good":"bad",
    "boy":"girl",
    "sir":"madam"
}
print(name["boy"])
for i in name:
    print(name)




boys_name=[["hassan",1],["ali",2],["ahmad",3],["bilal",4],["aliza",4]]
pos_boys=dict(boys_name)
# print(pos_boys)
for item,poss in pos_boys.items():
    print(item,poss)
random_list=[int,float,"hassan",2,3,68,8,90,4654]
for item in random_list:
    if str(item).isnumeric() and item > 6:
        print(item)
