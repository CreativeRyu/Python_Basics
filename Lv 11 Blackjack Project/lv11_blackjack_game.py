from art_blackjack import logo
import random
import game_script
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

print(logo)

player_hand = []
player_score = 0
dealer_hand = []
dealer_score = 0
card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
deck_length = len(card_deck)
isContinue = True
isGameOver = False


# Holt eine zufällige Karte aus dem Deck
def get_random_card(somebodysHand):
    #random.choice()
    random_index = random.randint(1, deck_length) - 1
    random_card = card_deck[random_index]
    somebodysHand.append(random_card)


# Berechnet den Gesamtpunktestand der Karten auf einer Hand
# Achtung bei dem Dealer ist das Ass immer 11 -> noch einbauen
def calculate_score(somebodysHand):
    if 11 in somebodysHand and sum(somebodysHand) > 21:
        somebodysHand.remove(11)
        somebodysHand.append(1)
    return sum(somebodysHand)


# Wertet die Ergebnisse des Spiels aus und prüft ob das Spiel weiter geführt werden kan
def game_controller(player_score, dealer_score, isGameOver):
    isDealersBlackjack = False
    isPlayersBlackjack = False

    if isGameOver:
        if dealer_score <= 21 and dealer_score > player_score:
            isDealersBlackjack = True
        elif player_score > dealer_score and player_score <= 21:
            isPlayersBlackjack = True
        elif dealer_score > 21 and player_score <= 21:
            isPlayersBlackjack = True
        elif dealer_score == player_score:
            isDealersBlackjack = True
            isPlayersBlackjack = True
        return show_game_result(isPlayersBlackjack, isDealersBlackjack)

    else:
        if player_score == 21 and dealer_score == 21 or dealer_score == 21 or player_score > 21:
            isDealersBlackjack = True
        elif player_score == 21:
            isPlayersBlackjack = True

        return show_game_result(isPlayersBlackjack, isDealersBlackjack)


# Zeigt das Ergebnis des Spiels in der Konsole an
def show_game_result(player_flag, dealer_flag):
    if dealer_flag and player_flag:
        print(game_script.text_draw)
        return True
    elif dealer_flag:
        print(game_script.text_lose)
        return True

    elif player_flag:
        print(game_script.text_win)
        return True
    else:
        return False


# Prüft ob eine weitere Karte vom Spieler gezogen werden soll
def validate_continue(continue_string):
    continue_string = continue_string.lower()

    if continue_string == "y":
        return True
    elif continue_string == "n":
        return False


# Zeigt die aktuellen Punkte und das Kartenblatt des Spielers an
def show_game_stats(hand, score):
    print(game_script.text_showCards)
    print(game_script.banner)
    print(f"{hand} Sie haben insgesamt {score} Punkte Sir.\n")
    print(game_script.banner)


# Main hier werden zu Beginn des Spiels zwei zufällige Karten auf die jeweilige Hand geholt
for _ in range(2):
    get_random_card(player_hand)
    get_random_card(dealer_hand)

# While Schleife zur Kontrolle des Spielflows
while isContinue and not isGameOver:
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    show_game_stats(player_hand, player_score)
    isGameOver = game_controller(player_score, dealer_score, isGameOver)
    if not isGameOver:
        print(f"Die erste Karte der Bank ist eine {dealer_hand[0]}")
        continue_string = input(game_script.text_moreCards)
        isContinue = validate_continue(continue_string)
        if isContinue:
            get_random_card(player_hand)

while dealer_score < 17:
    get_random_card(dealer_hand)
    dealer_score = calculate_score(dealer_hand)

player_score = calculate_score(player_hand)
game_controller(player_score, dealer_score, isGameOver)
print(
    f"Player: {player_hand} {player_score} Punkte | Dealer: {dealer_hand} {dealer_score} Punkte"
)