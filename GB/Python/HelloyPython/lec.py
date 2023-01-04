#Task5.3 Реализуйте алгоритм RLE: реализуйте модуль сжатия 
# и восстановления данных

v = input("Введите строку")




def cod(strr):
    countt=1
    collr = ''
    for i in range(len(strr)-1):
        if strr[i]==strr[i+1]:
            countt +=1
        else:
            collr = collr + str(collr) + strr[i]
            countt = 1
    if countt > 1 or (strr[len(strr)-2] != strr[-1]):
        collr = collr + str(countt)+strr[-1]
        return collr
 
def dec(strr):
    numm = ""
    collr = ""
    for j in range(len(strr)):
        if not strr[j].isalpha():
            numm += strr[j]
        else:
            collr = collr + strr[j] * int(numm)
            numm = ""
            return collr
c = cod(v)
d = dec(c)
print(f'кодированная строка:{c} декодированная строка: {d}')
