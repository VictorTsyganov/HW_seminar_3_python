# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]

new_list = []

for i in range(len(my_list)):
    new_element = round((my_list[i] - int(my_list[i])), 10)
    if new_element != 0:
        new_list.append(new_element)

print(max(new_list) - min(new_list))