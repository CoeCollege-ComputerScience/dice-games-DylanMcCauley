import random

def roll_die():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    die3 = random.randint(1, 6)
    die4 = random.randint(1, 6)
    die5 = random.randint(1, 6)
    die6 = random.randint(1, 6)
    die7 = random.randint(1, 6)
    die8 = random.randint(1, 6)
    die9 = random.randint(1, 6)
    die10 = random.randint(1, 6)
    print("You rolled a", die1, ",", die2, ",", die3, ",", die4, ",", die5, ",", die6, ",", die7, ",", die8, ",", die9, "and a", die10)
    return die1, die2, die3, die4, die5, die6, die7, die8, die9, die10  
    
def multiple_stays():
    print("Welcome to Multiple Stays!")
    print("You will roll ten dice.")
    print("Then the number of times each outcome was rolled.")
    print("You will then choose an outcome to remove from the dice and the remaining dice will be rolled again.")
    print("The game will end and you will lose once you can no longer remove multiples from the roll.")
    print (input("Please Press Enter to begin."))

    dice = list(roll_die())
    print(dice)
    print()
    while True:
        print("The number of times each outcome was rolled:")
        for i in range(1, 7):
            print(i, ":", dice.count(i))
        print()
        choice = int(input("Which outcome would you like to remove? "))
        if dice.count(choice) >= 2:
            dice.remove(dice.count(choice))
            print("You have removed all the", choice, "from the dice.")
            if len(dice) == 0:
                print("Congratulations! You have removed all the dice!")
                break
        else:
            print("Sorry! You do not have enough", choice, "to remove from the dice.")
            print("You lose!")
            break
        
        


   
        

    
multiple_stays()