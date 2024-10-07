
string = input().split(" ")
namber1 = float(string[0])
znak = string[1]
if znak == "M":
    result = (namber1 * 0.000621).__format__(".5f")
    print("Mile",result)
elif znak == "d":
    result = (namber1 * 39.3701).__format__(".5f")
    print("dyim",result)
elif znak == "y":
    result = (namber1 * 1.09361).__format__(".5f")
    print("yards",result)
else:
    print("Неккоректные данные")






























