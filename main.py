import art
import random

card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
WIN = 1
LOSE = -1
DRAW = 0

def in_hand(cards):
    score = 0
    for point in cards:
        score += point
    return score

def who_win(player_cards, computer_cards):
    player_score = in_hand(player_cards)
    computer_score = in_hand(computer_cards)
    while computer_score < 17:
        computer_cards.append(random.choice(card))
        computer_score = in_hand(computer_cards)
    print(f"Your final hand: {player_cards}, final score: {player_score}\n"
          f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    if player_score > 21:
        print("You went over. You lose 😭")
        return LOSE
    elif computer_score > 21 or player_score > computer_score:
        print("You win 😃")
        return WIN
    elif player_score == computer_score:
        print("Draw 🙃")
        return DRAW
    else:
        print("You lose 😤")
        return LOSE

def to_continue(player_cards, computer_cards):
    player_cards.append(random.choice(card))
    score = in_hand(player_cards)
    print(f"Your cards: {player_cards}, current score: {score}\n"
          f"Computer's first card: {computer_cards[0]}")
    return score

def check_threshold(score):
    if score > 21:
        return 1
    else:
        return 0


def play_blackjack():
    print(art.logo)

    player_cards = random.choices(card, k=2)
    computer_cards = random.choices(card, k=2)
    current_score = in_hand(player_cards)

    print(f"Your cards: {player_cards}, current score: {current_score}\n"
          f"Computer's first card: {computer_cards[0]}")
    answer = input("Type 'y' to get another card, type 'n' to pass: ")

    while answer == "y":
        current_score = to_continue(player_cards, computer_cards)
        if check_threshold(current_score):
            who_win(player_cards, computer_cards)
            break
        answer = input("Type 'y' to get another card, type 'n' to pass: ")

    if answer == "n":
        who_win(player_cards, computer_cards)

    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ")

    return play

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n' " )
while play == "y":
    play = play_blackjack()
if play != "y":
    print("You were amazing!")