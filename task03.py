# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов. (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random

my_random_list_len = int(input("Введите длину списка "))
min_random = float(input("Введите минимальное значение списка "))
max_random = float(input("Введите минимальное значение списка "))

def create_random_float_list(lenght, min, max):
    random_list = []
    for i in range(lenght):
        random_list.append(round(random.uniform(min, max), 2))
    return random_list

def find_fract_difference(some_list):
    for i in range(len(some_list)):
        some_list[i] = abs(some_list[i] - int(some_list[i]))
    return round((max(some_list) - min(some_list)), 2)

my_random_float_list = create_random_float_list(my_random_list_len, min_random, max_random)
print(my_random_float_list)
fract_difference = find_fract_difference(my_random_float_list)
print(f'Разница между максимальным и минимальным значением дробной части элементов равна {fract_difference}')
