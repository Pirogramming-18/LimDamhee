#1단계
num = 0

#2단계
cnt = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :')

#3단계

while(True):
    if not cnt.isdigit():
        print('정수를 입력하세요')
        cnt = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :')

    elif int(cnt) < 1 or int(cnt) >3:
        print('1,2,3 중 하나를 입력하세요')
        cnt = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :')
    else :
        break

#4단계
cnt = int(cnt)
sum = 0

player = 'A'
for i in range(cnt):
    print(f'player{player}: {i + 1}')

sum += cnt

#5단계
player = 'B' if player == 'A' else 'B'

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
    print(f'player{player}: {i + 1}')

sum += cnt

#6단계
#7단계
#8단계
#9단계