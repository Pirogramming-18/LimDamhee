num = 0
sum = 0
player = 'A'
flag = 0
while sum < 31:
    cnt = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :')

    while(True):
        if not cnt.isdigit():
            print('정수를 입력하세요')
            cnt = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :')

        elif int(cnt) < 1 or int(cnt) >3:
            print('1,2,3 중 하나를 입력하세요')
            cnt = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :')
        else :
            break

    cnt = int(cnt)

    for i in range(sum, sum + cnt):
        if i + 1 > 31:
            flag = 1
            break
        print(f'player{player}: {i + 1}')

    if flag == 1:
        break
    sum += cnt

    if player == 'A':
        player = 'B'
    else:
        player = 'A'

if player == 'A':
    print('player B win!')
else:
    print('player A win!')