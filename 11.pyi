
string = input("Видиье месяц и день через пробел").split(".")
namber1 = float(string[0])
namber2 = float(string[1])
if namber1 == "1":
    if namber2 == '1':
        print("понедельник")
else:
    print("плохл")

