# Eathan Hodgkinson
# This program simulates a modified version of Blackjack, where there is only one player and one dealer.

from deck import Deck
import time


def handValue(lst):
    total = 0
    for i in range(len(lst)):
        if lst[i].getRank() == "Jack" or lst[i].getRank() == "Queen" or lst[i].getRank() == "King":
            total += 10
        elif lst[i].getRank() == "Ace":
            total += 11
        else:
            total += lst[i].getCardValue()
    return total


def displayHand(lst):
    for i in range(len(lst)):
        print(lst[i])

    points = handValue(lst)

    if points > 21:
        print("Points: " + str(points) + "(Bust!)")
    else:
        print("Points: " + str(points))
    return


def main():
    playerBalance = 100

    while playerBalance > 0:
        print("\nYour balance: " + str(playerBalance))
        if playerBalance >= 5:
            betAmount = eval(input("How much do you want to bet? Enter a number from 5 to " + str(playerBalance) +
                                   ": "))
        else:
            betAmount = playerBalance
            print("\nYou had less than $5, so you had to bet all of it ($" + str(playerBalance) + ").")

        deck = Deck()
        deck.shuffle()
        hands = [[], []]

        for i in range(2):
            hands[0].append(deck.draw())
            hands[1].append(deck.draw())

        print("\nIt's your turn, and one of the dealer's cards is a " + str(hands[1][1]) + "...")
        print("\nYour hand:")
        displayHand(hands[0])

        while handValue(hands[0]) < 22:
            risk = eval(input("\nDo you want to take another card from the deck(1) or hold(2)?: "))

            if risk == 1:
                hands[0].append(deck.draw())
                print("\nYour hand:")
                displayHand(hands[0])
            elif risk == 2:
                break

        while True:
            print("\nDealer's turn. Their hand:")
            displayHand(hands[1])
            time.sleep(1)

            if handValue(hands[1]) < 17:
                hands[1].append(deck.draw())
                print("\nDealer drew a card.")
            elif 17 <= handValue(hands[1]) < 22:
                print("\nDealer holds.")
                break
            elif handValue(hands[1]) > 21:
                print("\nDealer busted!")
                break
        time.sleep(1)

        playerTotal = handValue(hands[0])
        dealerTotal = handValue(hands[1])
        win = False
        tie = False

        if dealerTotal == playerTotal:
            tie = True
        elif dealerTotal > 21 and playerTotal > 21:
            tie = True
        elif dealerTotal > playerTotal:
            if dealerTotal <= 21:
                win = False
            else:
                win = True
        elif dealerTotal < playerTotal:
            if playerTotal <= 21:
                win = True
            else:
                win = False

        if tie:
            print("\nYou and the dealer tied! Your balance is unchanged.")
        elif win:
            playerBalance += betAmount
            print("\nYou beat the dealer! $" + str(betAmount) + " has been added to your balance, which is now $" +
                  str(playerBalance) + ".")
        elif not win:
            playerBalance -= betAmount
            print("\nThe dealer beat you! $" + str(betAmount) + " has been removed from your balance, which is now $" +
                  str(playerBalance) + ".")

        if playerBalance > 0:
            print("\nBalance: " + str(playerBalance))
            replay = eval(input("Do you want to play again? Yes(1) or no(2)?: "))

            if replay == 2:
                print("\nThank you for playing and have a nice day!")
                break
        else:
            print("You are out of money! You can't play anymore.")
            break


main()
