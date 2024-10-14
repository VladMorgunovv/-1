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
# menager1 = int(string[0])
# menager2 = int(string[1])
# menager3 = int(string[3])

base = 200
percent = 0
premiya = 0
status = 0
if (int(string[0]) > int(string[1]) > int(string[2])
    or int(string[0]) > int(string[2]) > int(string[1])):
    status = 0
if (int(string[1]) > int(string[2]) > int(string[0])
    or int(string[1]) > int(string[0]) > int(string[2])):
    status = 1
if (int(string[2]) > int(string[1]) > int(string[0])
          or int(string[2]) > int(string[0]) > int(string[1])):
    status = 2
print(status)
k = 0
for i in string:
    zp = int(i)
    if 0 < zp < 500:
        percent = 0.03
    elif 500 <= zp < 1000:
        percent = 0.05
    elif zp >= 1000:
        percent = 0.08

    if k == status:
        premiya += 200
        print("Менеджер №:",k+1,",", base * (1 + percent) + premiya)
    else:
        print("Менеджер №:",k+1,",", base * (1 + percent))
    k+= 1













