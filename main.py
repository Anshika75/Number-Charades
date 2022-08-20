import random 
level = 1
attempt = 0
level = int(input("""Choose the level of difficulty: 
1 - Easy
2 - Intermediate
3 - Hard
4 - God
"""))
choice = 1
while choice == 1:
    if level == 1:
        limit = 50
    elif level <= 4:
        limit= 10**level
    else:
        print("Please enter correct level")
        exit()
    print(choice)
    print(limit)
    number = random.randint(1, limit)
    print(number)
    choice = int(input("""Enter 0 to exit
Enter 1 to restart
"""))

