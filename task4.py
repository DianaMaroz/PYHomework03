# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
try:
    dec_number = int(input("Введите целое число: "))
    def convert_dec_to_byn(num):
        byn_num = ''
        while num > 0:
            byn_num = str(num % 2) + byn_num
            num = num //2
        return byn_num
    print(f'{dec_number} -> {convert_dec_to_byn(dec_number)}')
except:
    print('Введены некорректные данные')

