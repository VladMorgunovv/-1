string = input()

numbers = string.split(" ")
#
# if len(numbers) == 4:
#     result = int(numbers[0]) * int(numbers[1]) * int(numbers[2]) * int(numbers[3])
#     print("* ", result)
# elif len(numbers) ==3:
#     result = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
#     print("+ ", result)
# elif len(numbers) < 1:
#     print("данные не введены")
# else:
#     result = (float(numbers[0]) / float(numbers[1])).__format__(" .4f")
#     print("/ ", result)
#     print("Введено 1 или 2 числа")
integer = len(numbers)

match integer:
    case 4:
        result = int(numbers[0]) * int(numbers[1]) * int(numbers[2]) * int(numbers[3])
        print(result)
    case 3:
        result = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
        print(result)
    case 2:
        result = (float(numbers[0]) / float(numbers[1])).__format__(" .4f")
        print(result)
    case 1:
        print("Данные не введены")
