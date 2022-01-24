def hangman(money, bet):
  import os
  import time
  import random
  
  def display(list_thing):
    holder_list = []
    for i in range(len(list_thing)):
      holder_list.append(list_thing[i])
      holder_list.append("  ")
    return (''.join(holder_list))

  words = ['australia', 'penguin', 'ventilation', 'somtimes', 'islands', 'myths', 'keyboard', 'mirror', 'television', 'towel', 'carpet', 'two']

  choice = input("Would you like to input your own list of words?\n").lower()

  if choice[0] == 'y':
      words_string = input("Seperate the words with commas: ")
      words = words_string.split(', ')
      theWord = random.choice(words).upper()
  elif choice[0] == 'n':
      theWord = random.choice(words).upper()

  lives = 7
  letters = list(theWord)
  lettersLeft = len(theWord)
  Hidden_Word = list('_' * len(theWord))
  guessed = []
    
  while lives > 0:
      os.system('clear')
      print('Remaining guesses: ' + str(lives))
      if lives == 7:
        print("         ┌─────────┐          ")
        print("         |         |          ")
        print("                   |          ")
        print("                   |          ")
        print("                   |          ")
        print("                   |          ")
        print("                   |          ")
        print("                   |          ")
        print("                   |          ")
        print("                   |          ")
        print("                   |          ")
        print("                   |          ")
        print("                   |          ")
        print(" ──────────────────────────── ")
        print("                              ")
      elif lives == 6:
        print("         ┌─────────┐          ")
        print("         |         |          ")
        print("      ┌─────┐      |          ")
        print("      |     |      |          ")
        print("      └─────┘      |          ")
        print("                   |          ")
        print("                   |          ")
        print("                   |          ")
        print("                   |          ")
        print("                   |          ")
        print("                   |          ")
        print("                   |          ")
        print("                   |          ")
        print(" ──────────────────────────── ")
        print("                              ")
      elif lives == 5:
        print("         ┌─────────┐          ")
        print("         |         |          ")
        print("      ┌─────┐      |          ")
        print("      |     |      |          ")
        print("      └─────┘      |          ")
        print("         |         |          ")
        print("         |         |          ")
        print("         |         |          ")
        print("         |         |          ")
        print("         |         |          ")
        print("                   |          ")
        print("                   |          ")
        print("                   |          ")
        print(" ──────────────────────────── ")
        print("                              ")
      elif lives == 4:
        print("         ┌─────────┐          ")
        print("         |         |          ")
        print("      ┌─────┐      |          ")
        print("      |     |      |          ")
        print("      └─────┘      |          ")
        print("         |  /      |          ")
        print("         | /       |          ")
        print("         |/        |          ")
        print("         |         |          ")
        print("         |         |          ")
        print("                   |          ")
        print("                   |          ")
        print("                   |          ")
        print(" ──────────────────────────── ")
        print("                              ") 
      elif lives == 3:
        print("         ┌─────────┐          ")
        print("         |         |          ")
        print("      ┌─────┐      |          ")
        print("      |     |      |          ")
        print("      └─────┘      |          ")
        print("      \  |  /      |          ")
        print("       \ | /       |          ")
        print("        \|/        |          ")
        print("         |         |          ")
        print("         |         |          ")
        print("                   |          ")
        print("                   |          ")
        print("                   |          ")
        print(" ──────────────────────────── ")
        print("                              ") 
      elif lives == 2:
        print("         ┌─────────┐         ")
        print("         |         |          ")
        print("      ┌─────┐      |          ")
        print("      |     |      |          ")
        print("      └─────┘      |          ")
        print("      \  |  /      |          ")
        print("       \ | /       |          ")
        print("        \|/        |          ")
        print("         |         |          ")
        print("         |         |          ")
        print("        /          |          ")
        print("       /           |          ")
        print("      /            |          ")
        print(" ──────────────────────────── ")
        print("                              ")
      elif lives == 1:
        print("         ┌─────────┐          ")
        print("         |         |          ")
        print("      ┌─────┐      |          ")
        print("      |     |      |          ")
        print("      └─────┘      |          ")
        print("      \  |  /      |          ")
        print("       \ | /       |          ")
        print("        \|/        |          ")
        print("         |         |          ")
        print("         |         |          ")
        print("        / \        |          ")
        print("       /   \       |          ")
        print("      /     \      |          ")
        print(" ──────────────────────────── ")
        print("                              ")     


      print("Letters Guessed: " + display(guessed) + '\n')
      print(display(Hidden_Word))
          
      if lettersLeft == 0:
        print('\nNice job! You win!')
        money += bet*2
        break

          
      guess = input('\nWhat letter will you guess?\n').upper()
      potential_life = 0

      if len(list(guess)) > 1:
        print("You can only guess one letter at a time!")
        time.sleep(0.75)
      elif len(list(guess)) < 1:
        print("You need to input something!")
        time.sleep(0.75)  
      else:
        if guess in guessed:
          print("You already guessed this letter! ")
          time.sleep(0.75)

        else:
          if guess.isalpha() == False:
            print("Please input a letter! ")
            time.sleep(0.75)
          else:
            for i in range(len(theWord)):
              if guess == letters[i]:
                Hidden_Word[i] = letters[i]
                lettersLeft -= 1
              else:
                potential_life += 1
            if potential_life == len(theWord):
              lives -= 1
            guessed.append(guess)

  if lives == 0:
      os.system('clear')     
      print("         ┌─────────┐          ")
      print("         |         |          ")
      print("      ┌─────┐      |          ")
      print("      |X _ X|      |          ")
      print("      └─────┘      |          ")
      print("      \  |  /      |          ")
      print("       \ | /       |          ")
      print("        \|/        |          ")
      print("         |         |          ")
      print("         |         |          ")
      print("        / \        |          ")
      print("       /   \       |          ")
      print("      /     \      |          ")
      print(" ──────────────────────────── ")
      print("                              ")
      print(display(letters))
      print('\nYou loose! The word was ' + theWord.lower() + ".")

  return money