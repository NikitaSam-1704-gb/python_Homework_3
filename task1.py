#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

#Пример:

#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

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
summ=0
for i in range(1,len(list_values),2):
    summ+=list_values[i]
print(f' Сумма значений не четных элементов массива {summ}, индексация начинается с 0 ')
print()
