############### # # # # # # # # # # # # # # # # # # # # ###############
############### # # # # Lv 11 Blackjack Project # # # # ###############
############### # # # # # # # # # # # # # # # # # # # # ###############

from art import logo
import random
import game_script

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
def calculate_score(somebodysHand):
    if 11 in somebodysHand and sum(somebodysHand) > 21:
        somebodysHand.remove(11)
        somebodysHand.append(1)
    return sum(somebodysHand)


# Prüft ob während des Spiels ein Blackjack zustande gekommen ist
def game_controller(player_score, dealer_score):
    if player_score == 21 and dealer_score == 21 or dealer_score == 21 or player_score > 21:
        return True
    elif player_score == 21:
        return True


# Prüft das Ergebnis am Ende des Spiels
def evaluate_game(player_score, dealer_score):
    isDealersBlackjack = False
    isPlayersBlackjack = False

    if dealer_score <= 21 and dealer_score > player_score:
        isDealersBlackjack = True
    elif player_score > dealer_score and player_score <= 21:
        isPlayersBlackjack = True
    elif dealer_score > 21 and player_score <= 21:
        isPlayersBlackjack = True
    elif dealer_score == player_score:
        isDealersBlackjack = True
        isPlayersBlackjack = True

    show_game_result(isPlayersBlackjack, isDealersBlackjack)


# Zeigt das Ergebnis des Spiels in der Konsole an
def show_game_result(player_flag, dealer_flag):
    if dealer_flag and player_flag:
        print(game_script.text_draw)
    elif dealer_flag:
        print(game_script.text_lose)
    elif player_flag:
        print(game_script.text_win)


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
    isGameOver = game_controller(player_score, dealer_score)
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
evaluate_game(player_score, dealer_score)
print(
    f"Player: {player_hand} {player_score} Punkte | Dealer: {dealer_hand} {dealer_score} Punkte"
)