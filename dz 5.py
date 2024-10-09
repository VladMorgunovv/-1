import calendar


# dayoweek = input("Видите номер дня")
#
# if dayoweek == "1":
#     print('понедельник')
# elif dayoweek == "2":
#     print("Вторник")
# elif dayoweek == "3":
#     print("Среда")
# elif dayoweek == "4":
#     print("Четвер")
# elif dayoweek == "5":
#     print("Пятница")
# elif dayoweek == "6":
#     print("Суббота")
# elif dayoweek == "7":
#     print("Воскрисение")
# else:
#     print("День не соотвестует")
string = input()
print(list(calendar.day_name)[int(string)])