#Урок 3. Данные, функции и модули в Python
#1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

def list_rand_nums(count: int) ->l:
    if count < 0:
      print("negative value of the numbers!")
      return[]
  
    list_nums = sample(range(1? count * 2), count)
    return list_nums


def sum_odd_pos(list_nums), 2):
    sum_nums = 0
    for k in range(0, len(list_nums), 2):
      sum_nums += list_nums[k]
    return sum_nums
  
  
