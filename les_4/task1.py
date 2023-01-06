# Вычислить число c заданной точностью d

import math #импорт модуля МАТЕМАТИКА
from decimal import Decimal #импорт модуля ....

# №1. конвертация ввода в input() в вид "1.000...."
def calcLevel(d):

    #  отрисовка кол-ва нулей, которое введено в input()
    arr1 = [0 for i in range( int(d) )]
    #print(arr1, type(arr1[0])) # ---> [0, 0, 0, 0] <class 'int'>

    # перерисовка в вид "1.00000"
    numer = ''
    for i in arr1:
        numer +=str(i)
    numer = '1.'+numer
    #print(numer, type (numer))

    return numer
  
