# Задание №2. Задача №1 вариант №2
# completed
# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# 6782 -> 23
# 0.67 -> 13
# 198.45 -> 27
#  
#
x = str(input('Введите число '))
str_x = str(x)
str_x = str_x.replace('-', '') # производим замену минуса на пробел
str_x = str_x.replace('.', '') # производим замену десятичной точки на пробел
lst_str = list(str_x) # строку с числом в список строк с цифрами
lst_num = map(int, lst_str) # преобразовываем каждый элемент полученного списка строк с цифрами в список целых чисел
s = sum(lst_num) # применяем функцию `sum()
print(f'сумма чисел в числе {x} равно {s}')
