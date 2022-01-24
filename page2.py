import random
import os

def change_attribute(card, value):
  card.value=value

def blackjack(money, bet):
  class Card: #I had this in a serepate file but the replay-ablility of War and Blackjack depended on the instances list being renewed every time the function was called, which wasn't happening, so I had to have to here instead
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
  
  os.system('clear')
  num = 0
  dealer_hand = []
  human_hand = []
  human_cards = 2
  dealer_cards = 2
  active_cards = []
  changed_cards = []
  the_cards = Card.instances
  
  while len(Card.instances) > 0:
    randIndex = random.randrange(len(the_cards))
    the_card = the_cards[randIndex]
    if the_card.value == 14:
      change_attribute(the_card, "11")
    elif the_card.value > 10:
      change_attribute(the_card, "10")
    if num % 2 == 1:
      human_hand.append(the_card)
    elif num % 2 == 0:
      dealer_hand.append(the_card)
    num += 1
    (Card.instances).remove(the_card)
  print("Your cards: \n" + str(human_hand[0].display + '\n' + str(human_hand[1].display)))
  print("The dealer's cards: \n" + str(dealer_hand[0].display + '\n' + "┌───────┐\n| ?     |\n|       |\n|   ?   |\n|       |\n|     ? |\n└───────┘"))
  
  total = 0
  choice = ' '

  while total <= 21 and choice[0] != 's':
    choice = input("Hit or stand? ").lower()
    total = 0
    if choice[0] == 'h':
      os.system('clear')
      human_cards += 1
      print('Your cards: ')
      for i in range(human_cards):
        print(human_hand[i].display)
        total += int(human_hand[i].value)
        active_cards.append(human_hand[i])
      if total > 21:
        while len(changed_cards) == 0:
          total = 0
          for i in range(len(active_cards)):
            if int(active_cards[i].value) == 11:
              change_attribute(active_cards[i], "1")
              total += int(active_cards[i].value)
              if total >= 21:
                pass
              else:
                changed_cards.append(active_cards[i])
            else:
              total += int(active_cards[i].value)
            changed_cards.append(active_cards[i])
      print("The dealer's cards: \n" + str(dealer_hand[0].display + '\n' + "┌───────┐\n| ?     |\n|       |\n|   ?   |\n|       |\n|     ? |\n└───────┘"))

    elif choice[0] == 's':
      pass
    else:
      choice = input("Pleas input hit or stand. ").lower()
    
  if total > 21:
    print('You busted! ')
    input('Press enter to initiate the dealer\'s cards. ')
    os.system('clear')
    busted = True
  elif choice[0] == 's':
    busted = False
    os.system('clear')

  total = 0
  changed_cards = []

  print('Your cards: ')
  for i in range(human_cards):
    print(human_hand[i].display)

  print('Dealer\'s cards: ')
  for i in range(dealer_cards):
    print(dealer_hand[i].display)
    total += int(dealer_hand[i].value)

  while total < 17:
    total = 0
    active_cards = []
    os.system('clear')
    dealer_cards += 1
    print('Your cards: ')
    for i in range(human_cards):
      print(human_hand[i].display)
    print('Dealer\'s cards: ')
    for i in range(dealer_cards):
      print(dealer_hand[i].display)
      total += int(dealer_hand[i].value)
      active_cards.append(dealer_hand[i])
    if total >= 17:
      while len(changed_cards) == 0:
        total = 0
        for i in range(len(active_cards)):
          if int(active_cards[i].value) == 11:
            change_attribute(active_cards[i], "1")
            total += int(active_cards[i].value)
            if total >= 17:
              pass
            else:
              changed_cards.append(active_cards[i])
          else:
            total += int(active_cards[i].value)
          changed_cards.append(active_cards[i])

  if total > 21:
    if busted == True:
      money += bet
      print("You both busted! Take your money back.")
    elif busted == False:
      money += bet*2
      print("You won! Congrats! Take twice them money you put in!")
  elif total <= 21:
    if busted == True:
      print("You lost. Unlucky. You lost your bet.")
    elif busted == False:
      human_total = 0
      for i in range(human_cards):
        human_total += int(human_hand[i].value)
      dealer_total = 0
      for i in range(dealer_cards):
        dealer_total += int(dealer_hand[i].value)
      if dealer_total > human_total:
        print("You lost. Unlucky. You lost your bet.")
      elif human_total > dealer_total:
        money += bet*2
        print("You won! Congrats! Take twice them money you put in!")     
      elif human_total == dealer_total:
        money += bet
        print("You tied! Take your money back.")   
  return money