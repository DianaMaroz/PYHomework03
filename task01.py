# 1.Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

my_random_list_len = int(input("Введите длину списка "))
min_random = int(input("Введите минимальное значение списка "))
max_random = int(input("Введите минимальное значение списка "))

def create_random_int_list(lenght, min, max):
    random_list = []
    for i in range(lenght):
        random_list.append(random.randint(min, max))
    return random_list

def count_odd_item(sm_list):
    count = 0
    for i in range(1, len(sm_list), 2):
        count += sm_list[i]
    return count

my_random_list = create_random_int_list(my_random_list_len, min_random, max_random)
print(my_random_list)
print(f'Сумма элементов списка на нечетной позиции равна {count_odd_item(my_random_list)}')

