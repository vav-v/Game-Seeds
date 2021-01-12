import math
import sys
print('   Игра Семечки\n')
mas = [[1,2,3,4,5,6,7,8,9],[1,1,1,2,1,3,1,4,1],[5,1,6,1,7,1,8,1,9]]
alf = tuple('абвгдежзи')
numbers = '1234567890'
lines = 3
masf = 0
mas1 = []
while True:
    print(' ' * (len(str(lines)) + 2) + 'А Б В Г Д Е Ж З И')
    for i in range(lines):
        print(str(i+1) + ')' + ' ' * (len(str(lines)) - len(str(i + 1))), end=' ')
        for n in range(len(mas[i])):
            if n < (len(mas[i]) - 1):
                print(str(mas[i][n]), end=' ')
            else:
                print(str(mas[i][n]))
    print('\n')
    num = input('Введите координату выбранной пары через пробел, например: А1 А2\nДля добавления чисел напишите: 0 0\n').lower().split(' ')
    try:
        if num[0] != num[1] and num[0] != '0' and num[1] != '0':
            idnum = alf.index(num[0][:1])
            idryad = int(num[0].replace(num[0][:1], '')) - 1
            idnum1 = alf.index(num[1][:1])
            idryad1 = int(num[1].replace(num[1][:1], '')) - 1
            if (mas[idryad][idnum] == mas[idryad1][idnum1] and mas[idryad][idnum] != 'x' and ((abs(idnum-idnum1) == 1 and abs(idryad-idryad1) == 0) or (abs(idnum-idnum1) == 0 and abs(idryad-idryad1) == 1))) or (mas[idryad][idnum] + mas[idryad1][idnum1] == 10 and mas[idryad][idnum] != 'x' and ((abs(idnum-idnum1) == 1 and abs(idryad-idryad1) == 0) or (abs(idnum-idnum1) == 0 and abs(idryad-idryad1) == 1))):
                print('\n')
                mas[idryad][idnum] = 'x'
                mas[idryad1][idnum1] = 'x'
            elif (mas[idryad][idnum] == mas[idryad1][idnum1] or mas[idryad][idnum] + mas[idryad1][idnum1] == 10) and mas[idryad][idnum] != 'x' and abs(idnum-idnum1) != 1 and abs(idryad-idryad1) == 0:
                count = 1
                for i in range(abs(idnum-idnum1) - 1):
                    if mas[idryad][i + 1 + min(idnum, idnum1)] == 'x' and count != 0:
                        count = 1
                    else:
                        count = 0
                if count == 1:
                    print('\n')
                    mas[idryad][idnum] = 'x'
                    mas[idryad1][idnum1] = 'x'
            elif (mas[idryad][idnum] == mas[idryad1][idnum1] or mas[idryad][idnum] + mas[idryad1][idnum1] == 10) and mas[idryad][idnum] != 'x' and abs(idnum-idnum1) == 0 and abs(idryad-idryad1) != 1:
                count = 1
                for i in range(abs(idryad-idryad1) - 1):
                    if mas[i + 1 + min(idryad, idryad1)][idnum] == 'x' and count != 0:
                        count = 1
                    else:
                        count = 0
                if count == 1:
                    print('\n')
                    mas[idryad][idnum] = 'x'
                    mas[idryad1][idnum1] = 'x'
        elif num[0] == '0' and num[1] == '0':
            linesbe = lines
            for i in range(lines):
                for n in range(9):
                    if mas[i][n] != 'x':
                        mas1.append(mas[i][n])
                    if len(mas1) == 9:
                        mas.append(mas1)
                        linesbe += 1
                        mas1 = []
            if len(mas1) >= 1:
                mas.append(mas1)
                linesbe += 1
                masf = 1
            else:
                masf = 0
            lines = linesbe
        while ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'] in mas:
            mas.remove(['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'])
            lines -= 1
        if mas == []:
            input('Вы выиграли, зачеркнув все цифры! Разработчик: vav-v\nВКонтакте: vk.com/vav_v')
            sys.exit()
    except:
        print('Неверно введены данные!')


