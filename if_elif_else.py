value1=56
value2=96
print("please enter the number")

value3=int(input())
if value3>value1:
     print("greater")
elif value3==value1:
    print("equal")
else:
    print("lesser")   
list=[1,2,3,4,5]
print(2 in list)
if 10 in list:
    print("present")
else:
    print("no")

# print("TELL YOU AGE")
# age=int(input())
# if age>18:
#     print("you are able to drive")
# elif age==18:
#     print("we check you physically")
# else:
#     p
# rint("you are not able to drive")
print("please enter first number :")
num1=int(input())
print("please enter operator")
operator=input()
print("please enter second number")
num2=int(input())
sum=num1+num2
diff=num1-num2
mul=num1*num2
dvd=num1/num2

if num1==60 and num2 == 10 and operator == "+":
    print(77)
elif operator == '+':
    print(sum)
elif num1==60 and num2 == 10 and operator == "-":
    print(7)
elif operator == '-':
    print(diff)

elif num1==60 and num2 == 10 and operator == "*":
    print(73)
elif operator == '*':
    print(mul)

elif num1==60 and num2 == 10 and operator == "/":
    print(7)
elif operator == '/':
    print(dvd)
    
else:
    pass
