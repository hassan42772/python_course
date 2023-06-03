print("ROCK PAPER SESSIOR GAME")
print("please enter you choice of player1")
player1=str(input())
print("please enter you choice of player2")
player2=str(input())
if player1=="sessior" and player2 == "paper":
    print("congularate player 1 win!")
elif player1=="paper" and player2=="sessior":
    print("congularate player 2 win! ")
elif player1=="rock" and player2 == "sessior":
    print("congularate player 1 win!")
elif player1=="sessior" and player2=="rock":
    print("congularate player 2 win!")
elif player1=="rock" and player2 ==" paper":
    print("congularate player 1 win!")
elif player1=="paper" and player2 ==" rock":
    print("congularate player 1 win!")
else:
    pass

