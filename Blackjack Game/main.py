############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from replit import clear
from art import logo

#Function that allows us to generate random card and return it.
def give_cards():
  """Generates a random card."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)

  return card

#This function allows us to sum all teh cards inside our card list and also to understand if with teh 2 initial cards we have won the game or if we have an 11 on the list and the sum is over 21, we replace teh 11 by a 1.
def sum_cards(card_list):
  """Funtion to do teh sum of all the card in the card list"""
  if sum(card_list) == 21 and len(card_list) == 2:
    return 0

  if sum(card_list) > 21 and 11 in card_list:
    card_list.remove(11)
    card_list.append(1)

  return sum(card_list)

#This function allows us to compare the score fromt he player with the computer and understand who has won the game.
def compare_lists(player_cards_sum, computer_cards_sum):
  """Funtion to compare the scores from teh player with the computer."""
  if player_cards_sum == computer_cards_sum and player_cards_sum < 21:
    return "It's a draw"
  elif player_cards_sum == 0:
    return "You have won with a Blackjack!"
  elif computer_cards_sum == 0:
    return "Computer has won with a Blackjack"
  elif player_cards_sum > 21:
    return "You have lost! Your score is over 21."
  elif computer_cards_sum > 21:
    return "You have won! Computer score is over 21."
  elif player_cards_sum > computer_cards_sum:
    return "You have won!"
  else: 
    return "You have lost!"

#Main function where we do our logic
def game():

  print(logo)
  
  #We define the player and computer list.
  player_cards = []
  computer_cards = []

  continue_game = False

  #Populate both lists with the 2 initial cards.
  for _ in range(2):
    player_cards.append(give_cards())
    computer_cards.append(give_cards())
  
  while not continue_game:
    #Calculate the sum of both lists
    player_cards_sum = sum_cards(player_cards)
    computer_cards_sum = sum_cards(computer_cards)
    
    print(f"Your card list is: {player_cards}, and the score is: {player_cards_sum}.")
    print(f"Computer's first card is: {computer_cards[0]}.")
    
    if player_cards_sum == 0 or computer_cards_sum == 0 or player_cards_sum > 21:
      continue_game = True
    else:
      play_another_card = input("Do you want another card? Type 'y' for yes and 'n' for no: ")
  
      if play_another_card == "y":
        player_cards.append(give_cards())
      else:
        continue_game = True
  
  #Continue taking cards from the deck for the computer.
  while computer_cards_sum != 0 and computer_cards_sum < 17:
    computer_cards.append(give_cards())
    computer_cards_sum = sum_cards(computer_cards)
  
  
  print(f"Your final card list is: {player_cards}, and the final score is: {player_cards_sum}.")
  print(f"Computer's final card list is: {computer_cards}, and the final score is: {computer_cards_sum}.")
  print(compare_lists(player_cards_sum, computer_cards_sum))

#Main function
while input("Do you want to play a game of Blackjack? Type 'y' for yes and 'n' for no: ") == "y":
  clear()
  game()
