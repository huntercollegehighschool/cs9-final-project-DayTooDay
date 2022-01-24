"""
Name(s): Joseph Garey and Alycia Hu
Name of Project: Hangman and Card Games
"""

from page1 import *
from page2 import *
from page3 import *
import os

money = 100
bet = 1

os.system('clear')
game = ' '

while game[0] != 'q':
  game = input("Which game would you like to play? War or Blackjack or Hangman? Or just quit? ").lower()
  os.system('clear')

  if len(game) == 0:
    print("You have to input something! ")
    game = ' '
    pass

  else:
    if game[0] != 'q':
      bet = int(input("You have " + str(money) + "$. How much money will you be betting? "))

      while bet > money:
        os.system('clear')
        bet = int(input("You can't bet more than you have! \nYou have " + str(money) + "$. How much money will you be betting? "))
      money -= bet
      os.system('clear')
        
      if game[0] == 'w':
        money = war(money, bet)

      elif game[0] == 'b':
        money = blackjack(money, bet)
          
      elif game[0] == 'h':
        money = hangman(money, bet)

      if money == 0:
        print("You ran out of money!")
        loan = input("Would you like to take out a loan of 100$? ").lower()
        os.system('clear')
        if loan[0] == 'y':
          money += 100
        else:
          break
    else:
      break
  
os.system('clear')
print("You ended with: " + str(money) + "$ \nThanks for playing!")