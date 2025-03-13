import random

def roll_die():
    return random.randint(1, 6)


def pig_dice_game():
    print("Welcome to Pig Dice Game!")
    print("Two players will take turns to roll a die.")
    print("The first player to reach 100 points wins.")
    print("Good luck!")

    player1_score = 0
    player2_score = 0

    while player1_score < 100 and player2_score < 100:
        player1_turn_score = 0
        while True:
            roll = roll_die()
            print("Player 1 rolled a", roll)
            if roll == 1:
                print("Player 1's turn is over.")
                player1_turn_score = 0
                break
            else:
                player1_turn_score += roll
                print("Player 1's turn score is", player1_turn_score)
                choice = input("Player 1, do you want to roll again or hold? (r/h): ")
                if choice == 'h':
                    break
        player1_score += player1_turn_score
        print("Player 1's score is", player1_score)

        if player1_score >= 100:
            break

        player2_turn_score = 0
        while True:
            roll = roll_die()
            print("Player 2 rolled a", roll)
            if roll == 1:
                print("Player 2's turn is over.")
                player2_turn_score = 0
                break
            else:
                player2_turn_score += roll
                print("Player 2's turn score is", player2_turn_score)
                choice = input("Player 2, do you want to roll again or hold? (r/h): ")
                if choice == 'h':
                    break
        player2_score += player2_turn_score
        print("Player 2's score is", player2_score)

    if player1_score >= 100:
        print("Congratulations Player 1! You win!")
    else:
        print("Congratulations Player 2! You win!")

pig_dice_game()

