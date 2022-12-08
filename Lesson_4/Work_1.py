# Вычислить число c заданной точностью d
# Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤ 10^{-10}$
#
# import math
# d = float(input('Введите точность d в диапазоне: 10^{-1} ≤ d ≤ 10^{-10}: '))
#
# if 10 ** -1 >= d >= 10 ** -10:
#     count = 0
#     while d != 1:
#         d *= 10
#         count += 1
#     print(round(math.pi, count))
# else:
#     print('Точность d не входит в допустимый диапазон!')


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#
# N = int(input('Введите натуральное число N: '))
# some_list = []
# for i in range(1, N + 1):
#     if N % i == 0:
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             some_list.append(i)
# print(*some_list, sep=', ')

# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
#
# from random import randint
#
# some_list = [randint(1, 20) for _ in range(10)]
# print(*some_list, sep=', ')
#
# new_list = []
# # [new_list.append(i) for i in some_list if i not in new_list]
# # print(f"Список из неповторяющихся элементов: {new_list}")
#
# for i in some_list:
#     count = 0
#     for j in some_list:
#         if some_list[i] == some_list[j]:
#             count += 1
#     if count < 1:
#         new_list.append(i)
# print(new_list)