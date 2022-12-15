#Задайте список из n элементов  заполненных цифрами из промежутка (-N,N). 
# Найдите произведение элементов на указанных позициях, позиции хранятся 
# в файле file.txt в одной строке одно число

num = 4 #int(input('Введите число: '))


import file as p
import file as n

lst = list((range(num*-1, num+1)))

def collector(x_1, x_2):
    r=1
    for i in lst:
        if x_2 <= int(i) <= x_1 and int(i) !=0 :
            r = r * abs(int(i))
    return r

print(f'произведение элементов на указанных позициях (за исключением "0") составляет :  {collector(x_1 = p.value_pos(num),x_2 = n.value_neg(num))}')

