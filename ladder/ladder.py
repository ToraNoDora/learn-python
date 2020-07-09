import sys
import math
import os
import random
import re

val = 1
# n = 4
# Ввод количества знаков
n = int(input('Введите число от 1 до 4: '))

# Объявление функции,  n и val - аргументы функции
def ladder(n, val):
   for i in range(n):
       # Пробелы
       res1 = " " *(n-i)
       # Значки
       res2 = "#" *val
       val = val+1
       # Вывод
       print(res1+res2)

ladder(n,1)



