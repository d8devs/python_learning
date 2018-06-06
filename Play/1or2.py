import random

WinningCount = 0
LosingCount = 0

print('''
    Welcome the D8 Random Game!
    You have only two chooise....
    1 or 2
    
    For Exit : 0
''')


def printScore():
    print('#'*33)
    print('''
    WON : {}
    LOSE : {}
    '''.format(WinningCount, LosingCount))
    print('#' * 33)

while True:

    randomNumber = random.randint(1, 2)

    answer = input("Your Chooise ? : ")
    answer = int(answer)

    if(answer == 0):
        exit();
    elif(answer == randomNumber):
        WinningCount = WinningCount +1
        print("You Won!")
        printScore()
    else:
        print("Sorry, Try Again")
        LosingCount = LosingCount + 1
        printScore()