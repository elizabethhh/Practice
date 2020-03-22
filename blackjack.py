#GUIDELINES FOR BLACKJACK
"""User Story: As a user I want to clearly see the cards dealt to me and to the dealer.

User Story: As a user I want to be able to choose to stay.

User Story: As a user I want to be able to choose to hit until I choose to stay or until I bust.

User Story: As a user I want to clearly see the sequence of moves made by the dealer.

User Story: As a user I want to clearly see who won and why.

User Story: As a user I want to be able to quit the game or go again after each cycle."""

"""Intermediate Challenge

User Story: As a user I want the game to incorporate a virtual chip/currency system to simulate real-life staking mechanics.

User Story: As a user I want to clearly see my chip stack, as well as that of the dealer.

User Story: As a user I want to be able to vary my bet according to the min/max betting rules.

Advanced Challenge

User Story: As a user I want to be able to choose to split my hand whenever possible.

User Story: As a user I want to be able to choose to double down whenever possible."""

#IMPORT STATEMENTS
from stack import Stack
import random

#VARIABLES
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']*4
user = []
dealer = []

#FUNCTIONS --> METHODS
#class Hand:
def calculateSum(hand):
    """
    Input: hand is a list of cards in user's hand
    Calculates the sum of cards in the user or dealer's hand
    Returns integer sum 
    """
    sum = 0
    for card in hand:  
        if card in ['J','Q','K']:
             sum += 10
        elif card == 'A':
            if sum >= 11: #when sum is greater than 11, Ace is no longer 11 because then it would bust the hand
                sum+= 1
            else:
                sum+= 11
        else:
            sum += card
    return sum

def hit(hand):
    """
    Input: hand is a list of cards in user's hand
    Gives person a new card (adds it to the list of cards in their hand)
    Unless they bust (over 21)
    """
    if not didBust(hand):
        newcard = cards.pop()
        hand.append(newcard)

    else:
        print("Sorry, you can't hit anymore. You have busted.")
    return hand

def didBust(hand):
    """Input: hand is a list of cards in user's hand
    Return boolean true if exceed 21
    """
    return calculateSum(hand) > 21


#GAME

#User Story: As a user I want to clearly see the cards dealt to me and to the dealer.
def blackjack():
    random.shuffle(cards)
    print(cards)
    print("User")
    for i in range(2):
        hit(user)
    print(user)

    print("Dealer")
    for i in range(2):
        hit(dealer)
    print(dealer)

    #User Story: As a user I want to be able to choose to stay.
    #User Story: As a user I want to be able to choose to hit until I choose to stay or until I bust.
    #User Story: As a user I want to clearly see the sequence of moves made by the dealer.

    while True:
        print("User total: " + str(calculateSum(user)))
        print("Dealer total: " + str(calculateSum(dealer)))
        choice = raw_input("Do you want to stay? Y or N. \n \n")
        if choice == "Y":
            print(hit(dealer))
            print("User total: " + str(calculateSum(user)))
            print("Dealer total: " + str(calculateSum(dealer)))
            if didBust(dealer):
                print("DEALER BUSTED! You win.")
                break
        elif choice == "N":
            print(hit(user))
            print("User total: " + str(calculateSum(user)))
            if didBust(user):
                print("USER BUSTED! You lose.")
                break
            else:
                print(hit(dealer))
                print("Dealer total: " + str(calculateSum(dealer)))
                if didBust(dealer):
                print("DEALER BUSTED! You win.")
                break
    
    #User Story: As a user I want to be able to quit the game or go again after each cycle.
    #reruns program if user answers Yes
    restart = input("Play again? Yes or No: ")
    if restart == "Yes" or restart == "yes":
        print()
        rps()
    else:
        print("Thanks for playing!")

#Start game
blackjack()



