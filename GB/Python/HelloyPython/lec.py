
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


numm = 40 #int(input('Введите натуральное число'))
r = range(1,numm)
lst = list(r)
result = 0
while result == numm:
    # if result == numm:
    #     result = i*x
    #     if result == numm:
    #         result = i*x*y
      for i in r[1:len(r)]:
         for x in r[1:len(r)]:
            for y in r[1:len(r)]:
                for m in r[1:len(r)]:
                    for z in r[1:len(r)]:
                    




# numm = 40 #int(input('Введите натуральное число'))

# s1 = ""
# n1=0
# n2=0
# cursor =" 1"
# correct=1
# l = list(range(1,numm))

# while int(cursor[len(cursor) - 2 : ]) < numm or int(cursor[len(cursor) - 2 : ]) > numm:
#     if int(cursor[len(cursor) - 2 : ]) > numm:
#         cursor =" 1"
#         i_correct = 0
#         correct+=1
#     for i in range(0,numm-1):
#         n1 =int(cursor[len(cursor) - 2 : ])
#         i_correct = int(i) + correct
#         s1 = int(cursor[len(cursor) - 2 : ]) * (int(i) + correct)
#         cursor += " " + str(s1) 
#         if int(cursor[len(cursor) - 3 : ]) > numm:
#             break



# print(f'int(cursor[-2:-1]){int(cursor[-2:-1])}')
# print(f'int(cursor[-2:-1]){int(cursor[-2:-1])} < numm{numm}')
# print(f'int(cursor[-2:-1]){int(cursor[-2:-1])} < numm{numm} or int(cursor[-2:-1]){int(cursor[-2:-1])} > numm {numm}:')
#     n1 = numm/l[i]
#     n2=0.2%(numm/l[i])
#     if  0==0.2%(numm/l[i]):
#             s1+=str(numm/int(l[i]))
#             numm/=numm/int(l[i])
#             print(s1)






# numm = 40 #int(input('Введите натуральное число'))

# s1 = ""
# n1=0
# n2=0
# l = list(range(1,numm))
# for i in range(0,numm-1):
#     n1 = numm/l[i]
#     n2=0.2%(numm/l[i])
#     if  0==0.2%(numm/l[i]):
#             s1+=str(numm/int(l[i]))
#             numm/=numm/int(l[i])
#             print(s1)
        # print(numm/l[i])
    
    #     s+=str(numm/l[i*-1])




# numm = 40 #int(input('Введите натуральное число'))

# s = ""
# l = list(range(1,numm))
# for i in range(1,numm):
#     if  0==2%(numm/l[i*-1]):
#         s+=str(numm/l[i*-1])

# 
# 
# if  0==2%(numm/int(lst[i*-1])):
#     s+=lst[i*-1].split()



# 
# 
# 
# 
#  numm = 40 #int(input('Введите натуральное число'))
# lst = list(range(0,numm-1))
# s = ""
# for i in lst:
#     print(lst[i*-1])
# #  if  0==2%(numm/int(lst[i*-1])):
# #     s+=lst[i*-1].split()


# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)* многочлена и записать в файл многочлен степени k.

#     *Пример:* 

#     - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#     -  k=5 => 2*x^5 + 4*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0
# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.(одинаковый размер уравнений)*

# *Доп задание: значения коэффициентов от -100 до 100
# *Доп задание: для разного размера уравнения

# Сдайте задание до: 22 дек., 20:00 +03:00 UTC
