n=10
# no of chances is 5
no_of_chances=1
while (no_of_chances <= 5):
    print("please enter tha gass no:")
    gass_no=int(input())
    if gass_no > n:
        print("please enter tha smaller no!")
    elif gass_no< n:
        print("please enter tha larger no!")
    else:
        print("you guess tha number")
        break
    print(5-no_of_chances,"remaning chances")
    no_of_chances=no_of_chances+1
if no_of_chances>5:
    print("game over")
      
        