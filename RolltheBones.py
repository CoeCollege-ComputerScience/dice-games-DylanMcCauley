import random

def roll_die():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    die3 = random.randint(1, 6)
    die4 = random.randint(1, 6)
    die5 = random.randint(1, 6)
    score = die1 + die2 + die3 + die4 + die5
    print("You rolled a", die1, die2, die3, die4, die5)
    return score

def roll_the_bones():
    print("Welcome to Roll the Bones!")
    print("To begin, you will make a guess about your total score of five dice accumulated.")
    print("You will then roll five dice.")
    print("Your score is the sum of the five dice.")
    print("If your guess is less than the total score, you will be rewarded with points equal to 5 less than your guess.")
    print("If your guess is equal to the total score, you will be rewarded with an astounding 50 points!")
    print("If your guess is greater than the total score, you will lose points equal to 5 minus your guess.")
    print("Good luck!")
    
    input("Press Enter to begin.")
    playerScore = 0
    playerTotal = 0
    turns = 0
    playerAveragePerTurn = 0
    while playerTotal < 1000000000000:
        turns += 1
        guess = int(input("What is your guess for the total score of five dice? "))
        playerScore = roll_die()
        print("The Addition of the dice =", playerScore)
        if guess < playerScore:
            reward = guess - 5
            print("Congratulations! You were correct! You have been rewarded with", guess - 5, "points.")
        elif guess == playerScore:
            reward = 50
            print("Congratulations! You were correct! You have been rewarded with 50 points!")
        else:
            reward = 5 - guess
            print("Sorry! You were incorrect! You have lost", 5 - guess, "points.")
        
        playerTotal += reward
        if turns == 1:
            playerAveragePerTurn = reward
        else:
            playerAveragePerTurn = playerTotal  / turns
        playerScore = 0
        reward = 0


        print("Your total score is", playerTotal)
        print("Your average score per turn is", playerAveragePerTurn)
        print()
        choice = input("Do you want to play again? (y/n): ")
        if choice == 'n':
            break
    
    print("Thank you for playing Roll the Bones!")

roll_the_bones()