# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def enter_parametr_array():
    number=int(input('Введите количество элементов N-> '))
    return number

def fill_ramdom_array():
    list_param=enter_parametr_array()
    list_values=[0]*list_param
    for i in range(list_param):
        list_values[i]=round((random.random()*10),2)
    return list_values
import random

list_values=fill_ramdom_array()
i=1
summ=0
max=list_values[0]%1
min=list_values[0]%1
while i<len(list_values):
    if max<list_values[i]%1:
        max=list_values[i]%1
    if min>list_values[i]%1:
        min=list_values[i]%1
    i+=1
summ=round((max-min),2)
print(f' {list_values} => {round((max-min),2)}')
print()

