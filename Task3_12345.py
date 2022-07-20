from decimal import Decimal
import random
import math
import types
from unicodedata import decimal
# 1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# def sum_of_odd_indices(len:int):
#     new_list = []
#     for i in range(len):
#         new_list.append(random.randint(1, 20))
#     result = new_list[1::2]  # срез с 1 индекса каждый второй
#     return ['В списке:{}'.format (new_list),'Элементы на нечетных позициях {}'.format (result),'Их сумма равна: {}'.format (sum(result))]

# len = int(input("Велечина списка:"))
# print(sum_of_odd_indices(len))  

# 2 - Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15] 

# def product_of_pairs_of_numbers():
#     new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     index1 = 0
#     my_list = []
#     while index1 < len(new_list)/2:
#         index2 = (index1+1)*-1
#         my_list.append(new_list[index1]*new_list[index2])
#         index1 += 1
#     return 'Произведение пар чисел:', my_list

# print(product_of_pairs_of_numbers())

# 3 - Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.567, 10.003] => 0.564 или 564  

# def fractional_part():
#     spisok = [1.1, 1.2, 3.1, 5.567, 10.003]
#     min = int(str(spisok[0]).split('.')[1])
#     max = int(str(spisok[0]).split('.')[1])
    
#     for i in range(len(spisok)):
#         buff = int(str(spisok[i]).split('.')[1])
#         if(max < buff):
#             max = buff
#         if(min > buff):
#             min = buff
#     result = max-min
#     return result

# print(fractional_part())


# 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# def binary(decimal):
#     result = ''
#     while decimal > 0:
#         result = str(decimal % 2) + result
#         decimal //= 2
#     return result
# while 1:
#     decimal = int(input('Ввести число:'))
#     if decimal != 0:
#         print(binary(decimal))
#     else:
#          break
        
# 5 - Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n: int):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    elif n == 2:
        return [0, 1, 1]

    li = fib(n-1)
    li.append(li[-1] + li[-2])
    return li


def recursive(n):
    fib_list = fib(n)
    negative_fib_list = []
    for i in range(1, len(fib_list)):
        if i % 2 == 0:
            negative_fib_list.append(fib_list[i] * -1)
        else:
            negative_fib_list.append(fib_list[i])
    return negative_fib_list[::-1] + fib_list


print(recursive(int(input('Введите число:'))))


