#Задайте список из n элементов  заполненных цифрами из промежутка (-N,N). 
# Найдите произведение элементов на указанных позициях, позиции хранятся 
# в файле file.txt в одной строке одно число
num = int(input('Введите число: '))
print(collector)

import file.value_pos as p
import file.value_neg as n

lst = list((range(num*-1, num+1)))
#print(lst)
# with open ('/home/vladi/Education/GB/Python/HelloyPython/my/S2/Task/file.py', 'a') as data:


x_1 = p.value_pos(nam)

x_2 = n.value_neg(nam)

def collector(x_1, x_2):
    for i in lst:
        if x_2 <= int(i) <= x_1:
            r = r + i
    return r

