#Задайте список из n элементов  заполненных цифрами из промежутка (-N,N). 
# Найдите произведение элементов на указанных позициях, позиции хранятся 
# в файле file.txt в одной строке одно число


lst = list((range(num*-1, num+1)))
#print(lst)
# with open ('/home/vladi/Education/GB/Python/HelloyPython/my/S2/Task/file.py', 'a') as data:


x_1 = value_pos(nam)
x_2 = value_neg(nam)

def collector(x_1, x_2):
    for i in lst:
        if x_2 <= int(i) <= x_1:
            r = r + i
    return r

num = int(input('Введите число: '))
print(collector)



# with open ('/home/vladi/Education/GB/Python/HelloyPython/my/S2/Task/Task2.4', 'a') as data:
#     data.write('#Задайте список из n элементов  заполненных цифрами из промежутка (-N,N). Найдите произведение элементов на указанных позициях, позиции хранятся в файле file.txt в одной строке одно число\n')
    
# num = int(input('Введите число: '))
# lst = list((range(num*-1, num+1)))
# # with open ('file.py','w') as data:
# #     data.write('def f(x,y):\n')
# #     data.write('    x = x/2\n')
# #     data.write('    return x\n')
# #     data.write('    y = y/2\n')
# #     data.write('    return y\n')
#
#
#     import \ThirdBigBranch20221123\file.py
# print(file.f(num*-1, num+1))


# num = int(input('Введите число: '))
# lst = list((range(num*-1, num+1)))
# with open ('file.py','w') as data:
#     data.write('def f(x,y):\n')
#     data.write('    x = x/2\n')
#     data.write('    return x\n')
#     data.write('    y = y/2\n')
#     data.write('    return y\n')









 







