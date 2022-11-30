# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input("Введите число: "))
def Fibonacci(num):
    if num > 0:
        if num in [1, 2]:
            return 1
        else:
            return Fibonacci(num-1) + Fibonacci(num-2)
    else:
        if num == -1:
            return 1
        else:
            return Fibonacci(num+2) - Fibonacci(num+1)

fib_list = [0]

for e in range (1, number + 1):
    fib_list.append(Fibonacci(e))
    fib_list.insert(0, Fibonacci(-e))
print(fib_list)
