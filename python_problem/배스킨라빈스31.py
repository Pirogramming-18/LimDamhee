from random import *

def brGame():
    cnt = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :')

    while (True):
        if not cnt.isdigit():
            print('정수를 입력하세요')
            cnt = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :')

        elif int(cnt) < 1 or int(cnt) > 3:
            print('1,2,3 중 하나를 입력하세요')
            cnt = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :')
        else:
            break

    return cnt

num = 0
player = 0
flag = 0

while num < 31:
    computer = randint(1,3)

    for i in range(num, num + computer):
        if i + 1 > 31:
            flag = 1
            break
        print(f'computer: {i + 1}')

    num += computer

    if flag == 1 or num >= 31:
        winner = 'player'
        break

    player = brGame()
    player = int(player)

    for i in range(num, num + player):
        if i + 1 > 31:
            flag = 1
            break
        print(f'player: {i + 1}')

    num += player

    if flag == 1 or num >= 31:
        winner = 'computer'
        break

print(f'{winner} win!')