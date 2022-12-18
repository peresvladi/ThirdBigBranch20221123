# 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдет разниу между между максимальным и минимальным 
# значением дробной  части элементов.
#    Пример: [1.1, 1.2, 3.1, 5.1, 10.01] 0.19

import time
def cosuale():
 rand_lst =list(str(int((time.time()%1)*100**8)))
 return rand_lst
lst1 = cosuale()[3 : 6]
lst2 = cosuale()[4 : 7]
lst = []
for i in lst1:
    for j in lst2:
        lst.append(i + "." + str((int(j)**2))) # задание списка вещественных чисел

maxx = round(((float(lst[-1]))%1), 3)
minn = round(((float(lst[-1]))%1), 3)

for el in lst:
    if maxx < (float(el))%1:
       maxx = (float(el))%1
    elif minn > (float(el))%1:
         minn = (float(el))%1
difference = maxx - minn
print(f'lst = {lst} \n{maxx}(maxx) - {minn}(minn)  = {difference}')
