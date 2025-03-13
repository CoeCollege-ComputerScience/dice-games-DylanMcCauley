import random

def roll_die():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    score = max(die1, die2) * 10 + min(die1, die2)
    print("You rolled a", die1, "and a", die2)
    return score

def beat_that():
    print("Welcome to Beat That!")
    print("You will roll two dice.")
    print("Your score is the higher die multiplied by 10 plus the lower die.")
    print("Good luck!")
    player1Score = 0
    player2Score = 0
    player1Total = 0
    player2Total = 0

    while player1Total < 100 and player2Total < 100:
        while player1Score < 100 and player2Score < 100:
            input("Press Enter to roll the dice for Player 1.")
            print(" Player 1: ")
            player1Score += roll_die()
            print("Player 1's score is", player1Score) 


            input("Press Enter to roll the dice for Player 2.")
            print(" Player 2: ") 
            player2Score += roll_die()
            print("Player 2's score is", player2Score)

            break

        if player1Score > player2Score:
            print("Congratulations Player 1! You win the round with a score of", player1Score)
            player1Total += player1Score

            
        elif player2Score > player1Score:
            print("Congratulations Player 2! You win the round with a score of", player2Score)
            player2Total += player2Score
        
        else:
            print("It's a tie! No one wins this round.")
        
        
        player1Score = 0
        player2Score = 0



        print("The current score is:")
        print("Player 1:", player1Total)
        print("Player 2:", player2Total)
        print()
        print("Next round!")



beat_that()

