#GUIDELINES FOR BLACKJACK


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
allcards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']*4

#CLASS PLAYER WITH METHODS
class Player:
    def __init__(self):
        self.cards = []
    
    def __str__(self):
        mycards = ""
        for card in self.cards:
            mycards += str(card) + " "
        return mycards

    def calculateSum(self):
        """
        Calculates the sum of cards in the user or dealer's hand
        Returns integer sum 
        """
        sum = 0
        for card in self.cards:  
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

    def hit(self):
        """
        Gives person a new card (adds it to the list of cards in their hand)
        Unless they bust (over 21)
        """
        if not self.didBust():
            newcard = allcards.pop()
            self.cards.append(newcard)

        else:
            print("Sorry, you can't hit anymore. You have busted.")
        return self.cards

    def didBust(self):
        """Input: hand is a list of cards in user's hand
        Return boolean true if exceed 21
        """
        return self.calculateSum() > 21

   


#GAME

#User Story: As a user I want to clearly see the cards dealt to me and to the dealer.
def blackjack():
    #create Player objects at start of game
    user = Player()
    dealer = Player()
    random.shuffle(allcards)
    print(allcards)

    #Deal 2 cards to user
    print("User")
    for i in range(2):
        user.hit()
    print(user)

    #Deal 2 cards to dealer
    print("Dealer")
    for i in range(2):
        dealer.hit()
    print(dealer)

    #User Story: As a user I want to be able to choose to stay.
    #User Story: As a user I want to be able to choose to hit until I choose to stay or until I bust.
    #User Story: As a user I want to clearly see the sequence of moves made by the dealer.

    while True:
        print("User total: " + str(user.calculateSum()))
        print("Dealer total: " + str(dealer.calculateSum()))
        choice = raw_input("Do you want to stay? Y or N. \n \n")
        if choice == "Y":
            dealerTotal = dealer.calculateSum()
            if dealerTotal>=17:
                #Dealer stays
                if user.calculateSum>dealer.calculateSum():
                    print("You win.")
                    break
                elif user.calculateSum==dealer.calculateSum():
                    print("You tied.")
                    break
                else:
                    print("Sorry! You lost.")
                    break
            else:
                print(dealer.hit())
                print("User total: " + str(user.calculateSum()))
                print("Dealer total: " + str(dealer.calculateSum()))
                if dealer.didBust():
                    print("DEALER BUSTED! You win.")
                    break
        elif choice == "N":
            print(user.hit())
            print("User total: " + str(user.calculateSum()))
            if user.didBust():
                print("USER BUSTED! You lose.")
                break
            else:
                print(dealer.hit())
                print("Dealer total: " + str(dealer.calculateSum()))
                if dealer.didBust():
                    print("DEALER BUSTED! You win.")
                    break
    
    #User Story: As a user I want to be able to quit the game or go again after each cycle.
    #reruns program if user answers Yes
    restart = raw_input("Play again? Yes or No: ")
    if restart == "Yes" or restart == "yes" or restart == "Y" or restart == "y":
        print()
        blackjack()
    else:
        print("Thanks for playing!")

#Start game
blackjack()



