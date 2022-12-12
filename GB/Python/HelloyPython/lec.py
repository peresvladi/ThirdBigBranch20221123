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


# l
lst = []
count = 0
def control(x = 0, y = 0):
    rng = range(x,y)
    if x < y:
       count = y - x
    else:
        count = x - y
    lst = list(rng)
    for i in lst:
           
        return lst[i]

print(control(0,6))





 











    # with open ('/home/vladi/Education/GB/Python/HelloyPython/my/S2/Task/Task2.4', 'a') as data:
    #     data.write('#Реализуйте механизм нахождения(генерации) рандомного (случайного) числа(Не используя библиотеки связанные с рандомом)\n')
    