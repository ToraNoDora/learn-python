import os
import sys



# Объявляем функцию getMoneySpent
def getMoneySpent(keyboards, drives, b):
    # Наибольший к клаве
    max_of_keyboards = max(keyboards)
    # наибольший к накопителям
    max_of_drives = max(drives)
    # Проверяет, одинаковы ли объекты
    maximum_of_keyboards_and_drives = max(max_of_keyboards, max_of_drives)
    # Множественное
    if(len(keyboards)==1 and len(drives)==1):
        if(max_of_keyboards+max_of_drives<b):
            return max_of_keyboards+max_of_drives
        else:
            return -1
    elif(maximum_of_keyboards_and_drives in drives and len(keyboards)!=1 and len(drives)!=1):
        while(maximum_of_keyboards_and_drives+max(keyboards)>b):
            keyboards.remove(max_of_keyboards)
            max_of_keyboards=max(keyboards)
        return maximum_of_keyboards_and_drives+max_of_keyboards


if __name__ == '__main__':
    # stdout - это уже открытый поток
    # C указателем: fptr = открыт ( ос . Environ [ 'OUTPUT_PATH' ], 'W' ) много мороки было. Поэтому заменил на данный вариант
    fptr = sys . stdout
    # Преобразование
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    # Максимальная сумма денег, которую Моника может потратить на оба товара, или возвращает - 1, если не может


    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()