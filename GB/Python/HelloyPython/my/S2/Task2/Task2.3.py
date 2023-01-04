#Задайте словарь из n чисел последовательности (1+(1\n)^n и выведите на экран их сумму
dictionary = {'1': 0, '2': 0, '3': 0}
j=0
s=[]
m=0.00
for i in dictionary.keys():
    j=j+1
    dictionary[i] = {round((1+1/j)**j, 3)}
    s = list(map(float, dictionary[i]))
    m=m+sum(s)
print(dictionary)
print(m)
