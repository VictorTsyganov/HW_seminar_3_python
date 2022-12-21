# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 4, 5, 6]

new_list = []

index_range = len(my_list) // 2

if len(my_list) % 2 != 0:
    index_range += 1

for i in range(index_range):
    new_list.append(my_list[0] * my_list[len(my_list) - 1])
    my_list = my_list[1 : ((len(my_list)) - 1)]

print(new_list)
