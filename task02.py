# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

import random

my_random_list_len = int(input("Введите длину списка "))
min_random = int(input("Введите минимальное значение списка "))
max_random = int(input("Введите минимальное значение списка "))

def create_random_int_list(lenght, min, max):
    random_list = []
    for i in range(lenght):
        random_list.append(random.randint(min, max))
    return random_list

def multiplicate_i_and_minus_i(some_list):
    multiplication_list = []
    if len(some_list) % 2 == 0:
        for i in range(len(some_list) // 2 ):
            multiplication_list.append(some_list[i] * some_list[-(1 + i)])
    else:
        for i in range(len(some_list) // 2 +1):
            multiplication_list.append(some_list[i] * some_list[-(1 + i)])
    return multiplication_list

my_random_list = create_random_int_list(my_random_list_len, min_random, max_random)
print(my_random_list)
print(multiplicate_i_and_minus_i(my_random_list))
