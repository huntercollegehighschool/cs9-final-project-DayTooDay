import random
import os

def change_attribute(card, value):
    card.player=value

def ShowCard(card):
    if card.face == None:
        print(str(card.number) + " of " + card.suit)
    else:
        print(str(card.face) + " of " + card.suit)
    print(card.display)

def war(money, bet):
  class Card:
      instances = []
      
      def __init__(self, suit, face, number, value, player, display):
          self.suit = suit
          self.face = face
          self.number = number
          self.value = value
          self.player = player
          self.display = display
          __class__.instances.append(self)

  card_1 = Card("Clubs", None, 2, 2, None, "┌───────┐\n| 2     |\n|       |\n|   ♣   |\n|       |\n|     2 |\n└───────┘")
  card_2 = Card("Clubs", None, 3, 3, None, "┌───────┐\n| 3     |\n|       |\n|   ♣   |\n|       |\n|     3 |\n└───────┘")
  card_3 = Card("Clubs", None, 4, 4, None, "┌───────┐\n| 4     |\n|       |\n|   ♣   |\n|       |\n|     4 |\n└───────┘")
  card_4 = Card("Clubs", None, 5, 5, None, "┌───────┐\n| 5     |\n|       |\n|   ♣   |\n|       |\n|     5 |\n└───────┘")
  card_5 = Card("Clubs", None, 6, 6, None, "┌───────┐\n| 6     |\n|       |\n|   ♣   |\n|       |\n|     6 |\n└───────┘")
  card_6 = Card("Clubs", None, 7, 7, None, "┌───────┐\n| 7     |\n|       |\n|   ♣   |\n|       |\n|     7 |\n└───────┘")
  card_7 = Card("Clubs", None, 8, 8, None, "┌───────┐\n| 8     |\n|       |\n|   ♣   |\n|       |\n|     8 |\n└───────┘")
  card_8 = Card("Clubs", None, 9, 9, None, "┌───────┐\n| 9     |\n|       |\n|   ♣   |\n|       |\n|     9 |\n└───────┘")
  card_9 = Card("Clubs", None, 10, 10, None, "┌───────┐\n| 10    |\n|       |\n|   ♣   |\n|       |\n|    10 |\n└───────┘")
  card_10 = Card("Clubs", "Jack", None, 11, None, "┌───────┐\n| J     |\n|       |\n|   ♣   |\n|       |\n|     J |\n└───────┘")
  card_11 = Card("Clubs", "Queen", None, 12, None, "┌───────┐\n| Q     |\n|       |\n|   ♣   |\n|       |\n|     Q |\n└───────┘")
  card_12 = Card("Clubs", "King", None, 13, None, "┌───────┐\n| K     |\n|       |\n|   ♣   |\n|       |\n|     K |\n└───────┘")
  card_13 = Card("Clubs", "Ace", None, 14, None, "┌───────┐\n| A     |\n|       |\n|   ♣   |\n|       |\n|     A |\n└───────┘")

  card_14 = Card("Diamonds", None, 2, 2, None, "┌───────┐\n| 2     |\n|       |\n|   ♦   |\n|       |\n|     2 |\n└───────┘")
  card_15 = Card("Diamonds", None, 3, 3, None, "┌───────┐\n| 3     |\n|       |\n|   ♦   |\n|       |\n|     3 |\n└───────┘")
  card_16 = Card("Diamonds", None, 4, 4, None, "┌───────┐\n| 4     |\n|       |\n|   ♦   |\n|       |\n|     4 |\n└───────┘")
  card_17 = Card("Diamonds", None, 5, 5, None, "┌───────┐\n| 5     |\n|       |\n|   ♦   |\n|       |\n|     5 |\n└───────┘")
  card_18 = Card("Diamonds", None, 6, 6, None, "┌───────┐\n| 6     |\n|       |\n|   ♦   |\n|       |\n|     6 |\n└───────┘")
  card_19 = Card("Diamonds", None, 7, 7, None, "┌───────┐\n| 7     |\n|       |\n|   ♦   |\n|       |\n|     7 |\n└───────┘")
  card_20 = Card("Diamonds", None, 8, 8, None, "┌───────┐\n| 8     |\n|       |\n|   ♦   |\n|       |\n|     8 |\n└───────┘")
  card_21 = Card("Diamonds", None, 9, 9, None, "┌───────┐\n| 9     |\n|       |\n|   ♦   |\n|       |\n|     9 |\n└───────┘")
  card_22 = Card("Diamonds", None, 10, 10, None, "┌───────┐\n| 10    |\n|       |\n|   ♦   |\n|       |\n|    10 |\n└───────┘")
  card_23 = Card("Diamonds", "Jack", None, 11, None, "┌───────┐\n| J     |\n|       |\n|   ♦   |\n|       |\n|     J |\n└───────┘")
  card_24 = Card("Diamonds", "Queen", None, 12, None, "┌───────┐\n| Q     |\n|       |\n|   ♦   |\n|       |\n|     Q |\n└───────┘")
  card_25 = Card("Diamonds", "King", None, 13, None, "┌───────┐\n| K     |\n|       |\n|   ♦   |\n|       |\n|     K |\n└───────┘")
  card_26 = Card("Diamonds", "Ace", None, 14, None, "┌───────┐\n| A     |\n|       |\n|   ♦   |\n|       |\n|     A |\n└───────┘")

  card_27 = Card("Spades", None, 2, 2, None, "┌───────┐\n| 2     |\n|       |\n|   ♠   |\n|       |\n|     2 |\n└───────┘")
  card_28 = Card("Spades", None, 3, 3, None, "┌───────┐\n| 3     |\n|       |\n|   ♠   |\n|       |\n|     3 |\n└───────┘")
  card_29 = Card("Spades", None, 4, 4, None, "┌───────┐\n| 4     |\n|       |\n|   ♠   |\n|       |\n|     4 |\n└───────┘")
  card_30 = Card("Spades", None, 5, 5, None, "┌───────┐\n| 5     |\n|       |\n|   ♠   |\n|       |\n|     5 |\n└───────┘")
  card_31 = Card("Spades", None, 6, 6, None, "┌───────┐\n| 6     |\n|       |\n|   ♠   |\n|       |\n|     6 |\n└───────┘")
  card_32 = Card("Spades", None, 7, 7, None, "┌───────┐\n| 7     |\n|       |\n|   ♠   |\n|       |\n|     7 |\n└───────┘")
  card_33 = Card("Spades", None, 8, 8, None, "┌───────┐\n| 8     |\n|       |\n|   ♠   |\n|       |\n|     8 |\n└───────┘")
  card_34 = Card("Spades", None, 9, 9, None, "┌───────┐\n| 9     |\n|       |\n|   ♠   |\n|       |\n|     9 |\n└───────┘")
  card_35 = Card("Spades", None, 10, 10, None, "┌───────┐\n| 10    |\n|       |\n|   ♠   |\n|       |\n|    10 |\n└───────┘")
  card_36 = Card("Spades", "Jack", None, 11, None, "┌───────┐\n| J     |\n|       |\n|   ♠   |\n|       |\n|     J |\n└───────┘")
  card_37 = Card("Spades", "Queen", None, 12, None, "┌───────┐\n| Q     |\n|       |\n|   ♠   |\n|       |\n|     Q |\n└───────┘")
  card_38 = Card("Spades", "King", None, 13, None, "┌───────┐\n| K     |\n|       |\n|   ♠   |\n|       |\n|     K |\n└───────┘")
  card_39 = Card("Spades", "Ace", None, 14, None, "┌───────┐\n| A     |\n|       |\n|   ♠   |\n|       |\n|     A |\n└───────┘")

  card_40 = Card("Hearts", None, 2, 2, None, "┌───────┐\n| 2     |\n|       |\n|   ♥   |\n|       |\n|     2 |\n└───────┘")
  card_41 = Card("Hearts", None, 3, 3, None, "┌───────┐\n| 3     |\n|       |\n|   ♥   |\n|       |\n|     3 |\n└───────┘")
  card_42 = Card("Hearts", None, 4, 4, None, "┌───────┐\n| 4     |\n|       |\n|   ♥   |\n|       |\n|     4 |\n└───────┘")
  card_43 = Card("Hearts", None, 5, 5, None, "┌───────┐\n| 5     |\n|       |\n|   ♥   |\n|       |\n|     5 |\n└───────┘")
  card_44 = Card("Hearts", None, 6, 6, None, "┌───────┐\n| 6     |\n|       |\n|   ♥   |\n|       |\n|     6 |\n└───────┘")
  card_45 = Card("Hearts", None, 7, 7, None, "┌───────┐\n| 7     |\n|       |\n|   ♥   |\n|       |\n|     7 |\n└───────┘")
  card_46 = Card("Hearts", None, 8, 8, None, "┌───────┐\n| 8     |\n|       |\n|   ♥   |\n|       |\n|     8 |\n└───────┘")
  card_47 = Card("Hearts", None, 9, 9, None, "┌───────┐\n| 9     |\n|       |\n|   ♥   |\n|       |\n|     9 |\n└───────┘")
  card_48 = Card("Hearts", None, 10, 10, None, "┌───────┐\n| 10    |\n|       |\n|   ♥   |\n|       |\n|    10 |\n└───────┘")
  card_49 = Card("Hearts", "Jack", None, 11, None, "┌───────┐\n| J     |\n|       |\n|   ♥   |\n|       |\n|     J |\n└───────┘")
  card_50 = Card("Hearts", "Queen", None, 12, None, "┌───────┐\n| Q     |\n|       |\n|   ♥   |\n|       |\n|     Q |\n└───────┘")
  card_51 = Card("Hearts", "King", None, 13, None, "┌───────┐\n| K     |\n|       |\n|   ♥   |\n|       |\n|     K |\n└───────┘")
  card_52 = Card("Hearts", "Ace", None, 14, None, "┌───────┐\n| A     |\n|       |\n|   ♥   |\n|       |\n|     A |\n└───────┘")

  skip = input("Remember, there is an end to this game. The cards will be tracked and put into one team's deck. Press enter to draw the next cards. \n\nYou can also type 'show human deck' or 'show computer deck' to see either team's cards. \n\nWould you like to manually press enter to go through the game? ").lower()

  while skip[0] != 'y' and skip[0] != 'n':
    skip = input("Please say yes or no. \n").lower()

  os.system('clear')
  
  human_cards = []
  computer_cards = []
  deck = True
  turns = 0
  num = 2

  while len(Card.instances) > 0:
    if num % 2 == 1:
      randIndex = random.randrange(len(Card.instances))
      HumanCard = Card.instances[randIndex]
      change_attribute(HumanCard, "human")
      human_cards.append(HumanCard)
      (Card.instances).remove(HumanCard)
      num += 1
    elif num % 2 == 0:
      randIndex = random.randrange(len(Card.instances))
      ComputerCard = Card.instances[randIndex]
      change_attribute(ComputerCard, "computer")
      computer_cards.append(ComputerCard)
      (Card.instances).remove(ComputerCard)
      num += 1

  while len(human_cards) and len(computer_cards) > 0:
    human_card = random.choice(human_cards)
    computer_card = random.choice(computer_cards)

    print("You drew: ")
    ShowCard(human_card)
    print("\nComputer drew: ")
    ShowCard(computer_card)
      
    if human_card.value > computer_card.value:
      print("\nYou win.")
      change_attribute(computer_card, "human")
      human_cards.append(computer_card)
      (computer_cards).remove(computer_card)
          
    elif computer_card.value > human_card.value:
      print("\nComputer won.")
      change_attribute(human_card, "computer")
      computer_cards.append(human_card)
      (human_cards).remove(human_card)

    elif computer_card.value == human_card.value:
      print("\nIt's a tie!\n\nTie breaker:")

      if len(human_cards) < 4 or len(computer_cards) < 4:
        print("Someone didn't have enough cards to bet, so all cards were returned. ")
      else:
        (human_cards).remove(human_card)
        human_card2 = random.choice(human_cards)
        (human_cards).remove(human_card2)
        human_card3 = random.choice(human_cards)
        (human_cards).remove(human_card3)
        (computer_cards).remove(computer_card)
        computer_card2 = random.choice(computer_cards)
        (computer_cards).remove(computer_card2)
        computer_card3 = random.choice(computer_cards)
        (computer_cards).remove(computer_card3)
        print("You bet: ")
        ShowCard(human_card2)
        print("\nComputer bet: ")
        ShowCard(computer_card2) 
        print("You drew: ")
        ShowCard(human_card3)
        print("\nComputer drew: ")
        ShowCard(computer_card3)
        if computer_card3.value > human_card3.value:
          print("\nThe Computer Wins. Unlucky.")
          computer_cards.extend([human_card, human_card2, human_card3])
          computer_cards.extend([computer_card, computer_card2, computer_card3])

        elif computer_card3.value < human_card3.value:
          print("\nYou Win! Congrats!")
          human_cards.extend([human_card, human_card2, human_card3])
          human_cards.extend([computer_card, computer_card2, computer_card3])

        else:
          print("Another tie, so everyone gets their cards back. ")
          human_cards.extend([human_card, human_card2, human_card3])
          computer_cards.extend([computer_card, computer_card2, computer_card3])

    print("______________")
    while deck == True:
      if skip[0] == 'y':
        deck = input("").lower()
      elif skip[0] == 'n':
        pass
      if deck == "show human deck":
        print("Your deck: ")
        for i in (human_cards):
          print(i.display)
        print("You have " + str(len(human_cards)) + " cards.")
        print("______________")
        input("")
      elif deck == "show computer deck":
        print("Computer deck: ")
        for i in (computer_cards):
            print(i.display)
        print("You have " + str(len(computer_cards)) + " cards.")
        print("______________")
        input("")
      else:
        deck = False
    os.system('clear')
    turns += 1
    deck = True
          
  if len(human_cards) == 0:
    print("You lost! It took " + str(turns) + " turns.")
  elif len(computer_cards) == 0:
    print("You win! It took " + str(turns) + " turns.")
    money += bet*2
  return money