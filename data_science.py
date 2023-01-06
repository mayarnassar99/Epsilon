# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 17:50:25 2023

@author: eldawlia
"""

import random

#choices


choices = {1 : "rock" , 2 : "paper" , 3 : "scisser" }
stop = True
while stop:
  computer_choice = [1 ,2 , 3]
  invalid_input = True
  while invalid_input :
    print("you can choice (1 = rock ) or (2 = paper ) or (3 = scisser )")
    user = (input("enter your choice"))
    if user.isdigit() :
      user = int(user)
      if user in range(1 ,4) :
        invalid_input = False
      else :
        print("only can you choices 1 or 2 or 3")
    else :
      print("only numbers allowed")


    user2 = choices[user]
    print(f"your choice is {choices[user]}")
    computer_choice.remove(user)
    comp_choice = random.choice(computer_choice)
    comp_new = choices[comp_choice]
    print( f"computer has choicen {comp_new}")

#game logic
    if (user == 1 and computer_choice == 2 ) or (user == 2 and computer_choice == 1 ) :
      print("paper wins")
      win_result = "paper" 
    elif (user == 1 and computer_choice == 3 ) or (user == 3 and computer_choice == 1 ) :
      print("rock wins")
      win_result = "rock"
    else :
      print("scisser wins")
      win_result = "scisser"


# wins
    if win_result == user2 :
      print("congrats , you win")
    else :
      print("computer wins , try again")
    stop_game = input("do you want play again ? if no pleas write 'n' ")
    if stop_game == "n" :
      stop = False
