import random 
level = 1
attempt = 0
choice = 1
chances = 10



while choice == 1:
    
    level = int(input("""Choose the level of difficulty: 
1 - Easy
2 - Intermediate
3 - Hard
4 - God
"""))
    if level == 1:
        chances = 10
        limit = 50
    elif level <= 4:
        chances = 15//level
        limit= 10**level
    else:
        print("Please enter correct level")
        exit()
    print("You have {} chances to guess the number in the range [1, {}]".format(chances,limit))
    print(choice)
    print(limit)
    number = random.randint(1, limit)
    print(number)
    choice = int(input("""Enter 0 to exit
Enter 1 to restart
"""))

