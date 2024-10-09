# for i in range(1,100):
#     if i % 3 == 1 and 40 < i < 50:
#         print(i)
#         # break
#
# else:
    print("Завершение")
    string = input('видите число черзе пробел и знак').split(" ")
    namber1 = float(string[0])
    namber2 = float(string[1])
    namber3 = float(string[2])
    znak = string[3]
    if znak == "+":
        result = namber1 + namber2 + namber2
        print(result)
    elif znak == "*":
        result = namber1 * namber2 * namber3
        print(result)
    elif znak == "-":
        result = namber1 - namber2 - namber3
        print(result)

    elif znak == "/":
        result = (namber1 / namber2 / namber3).__format__(".4f")
        print(result)
    else:
        print("Некоретное дpr")
    # from test import string
    # string = input('видите число черзе пробел и знак')
    # print(eval(string))
    from test import string, result

    # string = input("видите 3 числа ").split(" ")
    # nambers = []
    # for i in string:
    #     nambers.append(int(i))
    # print(max(nambers))
    # print(min(nambers))
    # print(sum(nambers) /len(nambers))n
