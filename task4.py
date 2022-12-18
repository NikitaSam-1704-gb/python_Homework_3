# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10



chislo=int(input('Введите число ->'))
number=chislo
code=str('')
while number!=0:
    code=str(number%2) + code
    number=int(number/2)
print(f'число {chislo} -> {code}')
 

