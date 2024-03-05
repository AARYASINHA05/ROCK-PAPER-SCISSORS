# -*- coding: utf-8 -*-
"""rock-paper-scissors

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wkhaK-5Z0iFfdFhN-4N1A5TxqOF5GE9I
"""

import random
#function for displaying the scores...
def view_scores():
  print()
  print("---------------- SCORES ----------------")
  print()
  print("COMPUTER'S SCORES = ",point_c)
  print(player_name+"'S SCORES = ",point_p)
  print()

#function for displaying the rules...
def display_rules():
  print()
  print("The Rules for the Game 'Rock - Paper - scissors' are as follows : ")
  print()
  print("The Rock is denoted by the character 'R' ")
  print("The paper is denoted by the character 'P' ")
  print("The pair of Scissors is denoted by the character 'S' ")
  print("Rock wins against scissors; paper wins against rock; and scissors wins against paper.")
  print("If both players select the same character, it is considered a tie. ")
  print("Player with maximum number of points wins the game.")
  print()

while True:
  print("READY TO PLAY THE GAME 'ROCK - PAPER - SCISSORS' ? (Y/N)")
  answer = input() #taking input from the user...

  if answer == 'n' or answer == 'N':#if the answer is n/N then it comes out of the game...
    break
  else:

    display_rules()

    print("---------------- LET'S BEGIN THE GAME !! ----------------")
    print()
    player_name = input("Enter your name : ").upper()
    number_of_rounds = int(input("Enter the number of rounds : "))
    print()

    choice_list = ['R','P','S']


    number_of_rounds_played = 0
    point_p = 0
    point_c = 0

    while number_of_rounds_played < number_of_rounds:
      print("Enter your choice (R/P/S) "+player_name+" : ",end=" ")
      player_choice = input().upper()
      print()

      computer_choice = random.choice(choice_list)

      while True:
        if player_choice in ['R','S','P']:
          break
        else:
          print("Enter your choice (R/P/S), again, "+player_name+" : ",end=" ")
          player_choice = input().upper()
          print()

      print()
      print("COMPUTER'S CHOICE = ",computer_choice)
      print(player_name+"'S CHOICE = "+player_choice)
      print()

      #conditions...
      if computer_choice == 'R' and player_choice == 'R':
        print("It's a tie.")
        print()
        view_scores()
        continue
      elif computer_choice == 'R' and player_choice == 'P':
        print("PAPER wins against ROCK. 1 points goes to "+player_name)
        point_p+=1
        view_scores()
      elif computer_choice == 'R' and player_choice == 'S':
        print("ROCK wins against SCISSORS. 1 points goes to Computer.")
        point_c+=1
        view_scores()
      elif computer_choice == 'S' and player_choice == 'S':
        print("It's a tie.")
        print()
        view_scores()
        continue
      elif computer_choice == 'S' and player_choice == 'P':
        print("SCISSORS wins against PAPER. 1 points goes to Computer.")
        point_c+=1
        view_scores()
      elif computer_choice == 'S' and player_choice == 'R':
        print("ROCK wins against SCISSORS. 1 points goes to "+player_name)
        point_p+=1
        view_scores()
      elif computer_choice == 'P' and player_choice == 'P':
        print("It's a tie.")
        print()
        view_scores()
        continue
      elif computer_choice == 'P' and player_choice == 'R':
        print("PAPER wins against ROCK. 1 points goes to Computer.")
        point_c+=1
        view_scores()
      elif computer_choice == 'P' and player_choice == 'S':
        print("SCISSORS wins against PAPER. 1 points goes to "+player_name)
        point_p+=1
        view_scores()

      number_of_rounds_played += 1

    #displaying if the player won or lost the game...
    if point_c>point_p:
      print("Sorry, you lost the game. Better luck next time :)")
      print()
    else:
      print("Congrats !! You won the game !!")
      print()