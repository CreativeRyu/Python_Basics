#from art import logo
import random
############### # # # # # # # # # # # # # # # # # # # # ###############
############### # # # # Lv 11 Blackjack Project # # # # ###############
############### # # # # # # # # # # # # # # # # # # # # ###############

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

#print(logo)

player_hand = []
player_score = 0
dealer_hand = []
dealer_score = 0
card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
deck_length = len(card_deck)
isContinue = True
isBlackjack = False


# Holt eine zufällige Karte aus dem Deck
def get_random_card(somebodysHand):
    #random.choice()
    random_index = random.randint(1, deck_length) - 1
    random_card = card_deck[random_index]
    somebodysHand.append(random_card)


# Berechnet den Gesamtpunktestand der Karten auf einer Hand
def calculate_score(somebodysHand):
    score = 0
    for card_score in somebodysHand:
        score = score + card_score

    return score


# Wertet die Ergebnisse des Spiels aus und prüft ob das Spiel weiter geführt werden kan
def game_controller(player_score, dealer_score):
    isDealersBlackjack = False
    isPlayersBlackjack = False

    if (player_score == 21 and dealer_score == 21) or dealer_score == 21:
        isDealersBlackjack = True

    elif player_score == 21:
        isPlayersBlackjack = True

    elif player_score > 21:
        if 11 in player_hand:
            for card in range(len(player_hand)):
                if player_hand[card] == 11:
                    player_hand[card] = 1
                    print("Das Ass können wir jedoch mit der Wertigkeit 1 betrachten.")
                    player_score = calculate_score(player_hand)
                    show_game_stats(player_hand, player_score)
                    game_controller(player_score, dealer_score)
        else:
            isDealersBlackjack = True

    if isDealersBlackjack:
        print(
            f"Sie haben verloren Sir, die Bank wird Ihren Reichtum leider einbehalten müssen. Wir hatten einfach die besseren Karten.\n{dealer_hand}"
        )
        return True

    elif isPlayersBlackjack:
        print("Sie haben gewonnen Sir, Sie werden großen Reichtum erlangen.")
        return True


def validate_continue(continue_string):
    continue_string = continue_string.lower()

    if continue_string == "y":
        return True
    elif continue_string == "n":
        return False

def show_game_stats(hand, score):
  print("Hier sind Ihre Karten")
  print("####################################\n")
  print(f"{player_hand} Sie haben insgesamt {player_score} Punkte Sir.\n")
  print("####################################\n")

for _ in range(2):
    get_random_card(player_hand)
    get_random_card(dealer_hand)

while isContinue and not isBlackjack:
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    show_game_stats(player_hand, player_score)
    isBlackjack = game_controller(player_score, dealer_score)
    if not isBlackjack:
        print(f"Die erste Karte der Bank ist eine {dealer_hand[0]}")
        continue_string = input("Möchten Sie eine weitere Karte ziehen Sir?\n")
        isContinue = validate_continue(continue_string)
    if isContinue:
        get_random_card(player_hand)
        get_random_card(dealer_hand)

print("### ENDE ###")
