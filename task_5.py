# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

number = int(input('Количество чисел положительной и отрицательной'
                   ' последовательностей Фибоначчи(min = 1): '))

fib_list = [0, 1]
count = 1

while count != number:
    fib_list.append(fib_list[len(fib_list) - 1]
                     + fib_list[len(fib_list) - 2])
    count += 1

neg_fib_list = [0, 1]
count = 1

while count != number:
    neg_fib_list.append(neg_fib_list[len(neg_fib_list) - 2]
                         - neg_fib_list[len(neg_fib_list) - 1])
    count += 1

print(neg_fib_list[:0:-1] + fib_list)