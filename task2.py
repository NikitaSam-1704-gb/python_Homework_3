# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from time import time

# print('Случайное число ',str(time())[-2:])
# print()

def enter_parametr_array():
    number=int(input('Введите количество элементов N-> '))
    min_value=int(input('Введите мин значение min-> '))
    max_value=int(input('Введите максимальное значение max-> '))
    return(number,min_value,max_value)

def fill_ramdom_array():
    list_param=enter_parametr_array()
    list_values=[0]*list_param[0]
    for i in range(list_param[0]):
        list_values[i]=int(random.randint(list_param[1],list_param[2]))
    return list_values
import random

list_values=fill_ramdom_array()
print(list_values, end=' ')
print()
if len(list_values)%2==0 :
    list_res=[0]*int(len(list_values)/2)
else:
    list_res=[0]*int(len(list_values)/2+1)
for i in range(len(list_res)):
    list_res[i]=list_values[i]*list_values[len(list_values)-1-i]
print(list_res, end=' ')
print()