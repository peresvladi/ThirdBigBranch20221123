# 1. Задайте список из нескольких чисел. Напишите программу, 
# которая найдет сумму элементов списка, стоящих на нечетных позициях.
#    Пример: [2, 3, 5, 9, 3] 3,9 ответ 12

import time
def cosuale():
 rand_lst =list(str(int((time.time()%1)*100**8)))
 return rand_lst
lst = cosuale()[5 : 10]
summ = 0
elem_summ = ""
for i in range(0,len(lst)-1,2):
    elem_summ += ("   "+lst[i+1])
    summ  += int((lst[i+1]))

print(f'в списке: {(lst)}, сумма елементов: {elem_summ}    стоящих на нечетных позициях \
составляет: {summ}')

