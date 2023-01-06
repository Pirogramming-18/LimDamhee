student_list = []

##############  menu 1
def Menu1(name, mid, final) :
    #사전에 학생 정보 저장하는 코딩
    student_list.append([name,mid,final])

##############  menu 2
def Menu2():
    for i in range(len(student_list)):
        if len(student_list[i]) < 4:
            avg = (int(student_list[i][1]) + int(student_list[i][2])) / 2
            avg = float(avg)
            if avg >= 90:
                g = 'A'
            elif avg >= 80:
                g = 'B'
            elif avg >= 70:
                g = 'C'
            else:
                g = 'D'
            student_list[i].append(g)

##############  menu 3
def Menu3():
    print('------------------------------')
    print('name     mid     final    grade')
    print('------------------------------')

    for i in range(len(student_list)):
        print(student_list[i][0].ljust(8), student_list[i][1].ljust(8), student_list[i][2].ljust(8), student_list[i][3].ljust(8))

##############  menu 4
def Menu4(del_name):
    for i in range(len(student_list)):
        if student_list[i][0] == del_name:
            del student_list[i]
            return 1

    return 0

print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")

while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        flag = 0
        #학생 정보 입력받기
        try:
            info = input('Enter name mid-score final-score : ')
            n, m, f = info.split()
        except:
            flag = 1
            print('Num of data is not 3!')

        if flag != 1:
            for i in range(len(student_list)):
                if (n == student_list[i][0]):
                    flag = 1
                    print('Already exist name!')

            if m.isdigit() == False or f.isdigit() == False:
                flag = 1
                print('Score is not positive integer!')
            #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)

            #예외사항이 아닌 입력인 경우 1번 함수 호출

        if flag != 1:
            Menu1(n, m, f)

    elif choice == "2" :
        #예외사항 처리(저장된 학생 정보의 유무)
        if not student_list:
            print('No student data!')
        else:
            Menu2()
            print('Grading to all students.')
        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력

    elif choice == "3" :
        flag = 0
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        if not student_list:
            print('No student data!')
        else:
            for i in range(len(student_list)):
                if len(student_list[i]) != 4:
                    print("There is a student who didn't get grade")
                    flag = 1
                    break

            if flag == 0:
                Menu3()
        #예외사항이 아닌 경우 3번 함수 호출

    elif choice == "4" :
    # 예외사항 처리(저장된 학생 정보의 유무)
    # 예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
    # 입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
    # 있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
        if not student_list:
            print('No student data!')
        else:
            del_name = input('Enter the name to delete: ')
            f = Menu4(del_name)
            if f == 1:
                print(f'{del_name}  student information is deleted.')
            else:
                print('Not exist name!')

    elif choice == "5" :
        #프로그램 종료 메세지 출력
        #반복문 종료
        print('Exit Program!')
        break
    else :
        #"Wrong number. Choose again." 출력
        print("Wrong number. Choose again.")