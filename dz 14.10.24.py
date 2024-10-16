# string =input()
#
# if 0 < int(string) > 100:
#     print("Веденое число вне дипозона")
# else:
#     namber = int(string)
#     if namber % 3 == 0 and namber % 5 != 0:
#         print("fizz")
#     elif namber % 5 == 0 and namber % 3 != 0:
#         print("Buzz")
#     elif namber % 15 == 0:
#         print("fizz Buzz")
#     else:
#         print(namber)



# string = input("видите число и степень:").split(" ")
#
# namber = int(string[0])
# stepen = int(string[1])
#
# if stepen >=0 and stepen <=7:
#     result = namber ** stepen
#     print(result)


# string = input("Стоимость, с кого звоним и куда звоним").split(" ")
# price =float(string[0])
# mtcot2 = 0
# mtcob = 1
# ttob = 2
# mtsom = 3
# btob = 4
# t2ot2 = 5
# if  string[1] == "m" and string[2] == 't':
#     result =price * 0.2
#     print(result)
#     """
#     TO DO
#     """


string = input().split(" ")
number = []
volume_all = []
for i in string:
    volume_all.append(int(i))

premia = 200
max_volume = 0
print(string)
index_manager = 0
for i in string:
    volume = int(i)
    zp = 200

    if 0 < volume < 500:
        zp *= 1.03
    elif 500 <= volume <= 1000:
        zp *= 1.05
    elif volume > 1000:
        zp *= 1.08
    number.append(zp)


count_max = 0
for i in string:
    max_volume = max(volume_all)
    if max_volume == int(i):
        count_max += 1
print(count_max)

k = 0
for i in string:
    max_volume = max(volume_all)
    print(max_volume)
    if max_volume == int(i):
        print("макс объем", )
        number[k] += premia / count_max
    k += 1
print(number)










