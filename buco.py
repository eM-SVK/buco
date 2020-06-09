import random
print('=' * 40)
print("Hi! Let's play a bulls and cows game")
print('=' * 40)

number = []

def makenum():
    for i in range(4):
        x = random.randrange(0, 9)
        number.append(x)
    if len(number) > len(set(number)):
        number.clear()
        makenum()

def game():
    bulls = 0
    cows = 0
    enter = input('Enter a number: ')
    player = []
    for i in range(4):
        player.append(int(enter[i]))
    for i in range(4):
        for j in range(4):
            if player[i] == number[j]:
                cows += 1
    for i in range(4):
        if player[i] == number[i]:
            bulls += 1
    print(f"{bulls} bulls, {cows} cows")
    if bulls != 4:
        game()

makenum()
game()