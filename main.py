
import random

choice = 1

while choice == 1:
    level = int(
        input(
            """
Choose the level of difficulty: 
1 - Easy
2 - Intermediate
3 - Hard
4 - God
"""
        )
    )
    if level == 1:
        chances = 10
        limit = 50
    elif level <= 4:
        chances = 15 // level
        limit = 10 ** level
    else:
        print("Please enter correct level")
        exit()
    print(
        "You have {} chances to guess the number in the range [1, {}]".format(
            chances, limit
        )
    )
    comp = random.randint(1, limit)
    while chances > 0:
        guess = int(input("Enter your guess: "))
        if guess == comp:
            print("You Won")
            break
        elif guess > comp:
            if guess - comp < limit // 5:
                print("You Guess Slightly High Number")
            else:
                print("You Guessed High Number")
        else:
            if comp - guess < limit // 5:
                print("You Guess Slightly low Number")
            else:
                print("You Guessed Low Number")
        chances -= 1
        if chances == 0:
            print("You idiot, lost the game")
            break
        print(f"{chances} chances left")
    print("Number Is : ", comp)
    choice = int(
        input(
            """Enter 0 to exit
Enter 1 to restart
"""
        )
    )

