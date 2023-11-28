import random

#функция красивого вывода массива
def print_mas(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])): print(arr[i][j], end=' ')
        print()


#функция генерации островов
def gen_islands(mas):
    for i in range(len(mas)):
        if i % 3 == 0: mas[i][random.randint(0, len(mas[i])-1)] = 1
        for j in range(len(mas[i])-1):
            if i != 0:
                if mas[i-1][j] == 1 or mas[i][j] == 1:


                    ################## блок кода для окончания отрисовки острова с шансом в 1/5 ##########################

                    num = random.randint(1, 5)
                    # вариант окончания №1
                    if num == 1 and mas[i-1][j+1] != 1: mas[i][j+1] = 1; mas[i][j] = 1; continue
                    # вариант окончания №2
                    elif num == 1 and mas[i-1][j+1] == 1:
                        if j != 0: mas[i][j-1] = 1; mas[i][j] = 1;continue
                        else: mas[i][j] = 1; continue

                    ################## блок кода для окончания отрисовки острова с шансом в 1/4 закончен #####################


                    ############### блок кода для отрисовки ######################

                    else:
                        #рандомное число для определения по какому варианту будет разростаться/уменьшаться остров
                        num1 = random.randint(1, 3)

                        #первый модуль распространения
                        if num1 == 1:

                            #первый вариант
                            if j != 0: mas[i][j] = 1; mas[i][j - 1] = 1

                            #второй вариант
                            else: mas[i][j] = 1

                        #третий вариант
                        elif num1 == 2: mas[i][j] = 1; break

                        #третий молдуль распространения
                        else:
                            num2 = random.randint(1, 3)

                            #четвертый вариант
                            if num2 == 1 and j != len(mas[i])-2: mas[i][j] = 1; mas[i][j+1] = 1; mas[i][j+2] = 1

                            #пятый вариант
                            elif num2 == 2 and j >= 2: mas[i][j] = 1; mas[i][j-1] = 1; mas[i][j-2] = 1

                            #шестой вариант
                            else:
                                if random.randint(1, 2) == 1: mas[i][j] = 1; mas[i][j+1] = 1
                                else:
                                    if j != 0: mas[i][j] = 1; mas[i][j-1] = 1
                                    else: mas[i][j] = 1

                    ############################### блок кода для отрисовки закончен #############################

    #возращаем сгенерированную карту
    return mas

def gen_island(mas):
    for i in range(len(mas)):
        for j in range(len(mas[i])):
            #с шансом в 1/3 делаем рандомное число строки однеркой
            r1 = random.randint(1, 3)
            if r1 == 1:
                mas[i][random.randint(0, 9)] = 1
            ##########
#генерация
            if i != 0:
                if mas[i-1][j] == 1:
                    #с шансом в 1\5 остров заканчивается
                    r2 = random.randint(1, 5)
                    if r2 == 1:
                        break
                    else:
                        #есть пять вариантов распространения
                        r3 = random.randint(1, 5)
                        match r3:
                            case[1]:
                                mas[i][j] == 1; mas[i][j+1] = 1
                            case[2]:
                                mas[i][j] == 1; mas[i][j-1] = 1
                            case[3]:
                                if j <= len(mas)-3:
                                    mas[i][j+1] == 1; mas[i][j+2] = 1
                                else:
                                    mas[i][j] = 1
                            case[4]:
                                if j >= 2:
                                    mas[i][j-1] = 1; mas[i][j-2] = 1
                                else:
                                    mas[i][j] = 1
                            case[5]:
                                mas[i-1][j+1] = 1
            ########### генерация закончилась

    return mas

#функция для измерения периметра островов
def find_P(mas):
    p = 0
    for i in range(len(mas)):
        for j in range(len(mas[i])):
            if j == 0 and mas[i][j] == 1 or mas[i][j] == 1 and mas[i][j-1] == 0: p+=1
            if i == 0 and mas[i][j] == 1 or mas[i][j] == 1 and mas[i-1][j] == 0: p+=1
            if j != len(mas[i])-1 and mas[i][j] == 1 and mas[i][j+1] == 0 or j == len(mas[i])-1 and mas[i][j] == 1: p+=1
            if i != len(mas)-1 and mas[i][j] == 1 and mas[i+1][j] == 0 or i == len(mas)-1 and mas[i][j] == 1: p+=1
    return p

#функция нахождения площади островов
def find_S(mas):
    s = 0
    for i in range(len(mas)):
        for j in range(len(mas[i])):
            if mas[i][j] == 1: s+=1
    return s


#создаем массив по введенным данным заполненный нулями
height = int(input('введите длину карты: '))
arr = [[0 for i in range(10)] for i in range(height)]

#выводим сгенерированную карту
while True:
    try:
        change = int(input('введите вид генерации карты(расспчатый - 1; кучный - 2): '))
        break
    except ValueError:
        print('введите числовое значение!!')
#проверка выбора пользователя и генерация
if change == 1:
    arr = gen_island(arr); print_mas(arr)
else:
    arr = gen_islands(arr); print_mas(arr)

#выводим периметр и площадь островов на карте
print(f"площадь всех островов: {find_S(arr)}", f"\nпериметр всех островов: {find_P(arr)}")
