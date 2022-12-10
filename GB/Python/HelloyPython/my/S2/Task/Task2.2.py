#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

num = int(input('Введите число :'))
rng = range(1,num + 1)
lst = list(rng)
result = 1
for j in lst:
    result=result*int(j)
    print(result)
