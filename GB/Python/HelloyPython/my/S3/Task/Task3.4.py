# 4. Напишите программу. которая будет преобразовывать десятичное число в двоичное.
#    Пример: 45 101101
#            3  11
#            2  10

decimal_number = int(input("введите число в десятичном формате: "))
binary_number2 = ""
while decimal_number >= 1:
    binary_number1 = (decimal_number % 2)
    binary_number2 = str(binary_number1) + " " + binary_number2
    decimal_number = int(decimal_number / 2)
print(f'число преобразованное в двоиченый формат   ===>    {binary_number2}')