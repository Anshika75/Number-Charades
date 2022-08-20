import random 
number = random.randint(1, 100)
print(number)
level = 1
attempt = 0
level = int(input("""Choose the level of difficulty: 
1 - Easy
2 - Intermediate
3 - Hard
4 - God
"""))
if level == 1:
    limit= [0, 50]
elif level <= 4:
    limit= [0, 10**level]
else:
    print("Please enter correct level")
    exit()
print(limit)