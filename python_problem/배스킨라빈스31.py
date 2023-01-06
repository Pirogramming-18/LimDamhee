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
playerA = 0
playerB = 0
flag = 0

while num < 31:
    playerA = brGame()
    playerA = int(playerA)

    for i in range(num, num + playerA):
        if i + 1 > 31:
            flag = 1
            break
        print(f'playerA: {i + 1}')

    num += playerA

    if flag == 1 or num >= 31:
        winner = 'player B'
        break

    playerB = brGame()
    playerB = int(playerB)

    for i in range(num, num + playerB):
        if i + 1 > 31:
            flag = 1
            break
        print(f'playerB: {i + 1}')

    num += playerB

    if flag == 1 or num >= 31:
        winner = 'player A'
        break

print(f'{winner} win!')