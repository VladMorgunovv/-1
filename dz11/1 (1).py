# expression = input("Введите арифметическое выражение ")
#
# parts = expression.split()
#
# if len(parts) == 3:
#
#     num1 = float(parts[0])
#
#     operator = parts[1]
#
#     num2 = float(parts[2])
#
#
#     if operator == '+':
#
#         result = num1 + num2
#
#     elif operator == '-':
#
#         result = num1 - num2
#
#     elif operator == '*':
#
#         result = num1 * num2
#     elif operator == '//':
#
#         result = num1 // num2
#
#     elif operator == '**':
#
#         result = num1 ** num2
#     elif operator == '%':
#
#         result = num1 % num2
#
#     elif operator == '/':
#
#         if num2 == 0:
#
#             print("Ошибка: деление на ноль.")
#
#         else:
#
#             result = num1 / num2
#
#     else:
#
#         print("Ошибка: неверный оператор.")
#
# else:
#
#     print("Ошибка: неверный формат ввода.")
#
#
# print("Результат:", result)

import random
random_list = [random.randint(-10, 10) for _ in range(10)]

min_value = min(random_list)

max_value = max(random_list)


negative_count = sum(1 for num in random_list if num < 0)

positive_count = sum(1 for num in random_list if num > 0)

zero_count = sum(1 for num in random_list if num == 0)



print("Сгенерированный список:", random_list)

print("Минимальный элемент:", min_value)

print("Максимальный элемент:", max_value)

print("Количество отрицательных элементов:", negative_count)

print("Количество положительных элементов:", positive_count)

print("Количество нулей:", zero_count)