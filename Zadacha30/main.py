# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


print('\n''Программа заполняет (и выводит) список арифметичской прогрессии: n = a1 + (n-1) * d у.''\n')

a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите шаг арифметической прогресси: "))
count = int(input("Введите количество элементов прогрессии: "))
progr = []
print('\n', "Полученная последовательность:")
# for i in range(count):
#     progr.append(a1 + i * d) 
# print(progr)

print((progr := [(a1 + i * d) for i in range(count)]))




