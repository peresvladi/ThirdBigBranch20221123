# 2.  Напишите программу, которая найдет произведение пар чисел списка. Парой считаем первый последний элемента, второй и предпоследний и т.д.
# 	Пример: [2,3,4,5,6] [12, 15, 16]

import time
def cosuale():
 rand_lst =list(str(int((time.time()%1)*100**8)))
 return rand_lst
lst = cosuale()[4 : 10]
summ = 0

print(f'список : {(lst)}')

if (int(len(lst)/2)%2)== 0: 
    print(f' произведение пар чисел списка {[int((lst[i]))*int((lst[(i+1)*-1])) for i in range(0, int(1+len(lst)/2))]}')
else:
    print(f' произведение пар чисел списка {[int((lst[i]))*int((lst[(i+1)*-1])) for i in range(0, int(len(lst)/2))]}')
