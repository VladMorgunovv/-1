# costomer = ['bob', 'Anna', "Joe", "Bob", "Nick"]
# # result = ""
# # for i in costomer:
# #     result += i + " "
# #     print(i)
# # print(result.rstrip(" ").split("")[:3]
# a1 = 10
# b1 = 20
# matrix =[[1,2,3],[4,5,6],[7,8,9],[a1,[13,14,[15,16,"OK"]],12, b1]]
# cearch = "OK"
# for i in matrix:
#     print("уровень", i)
#     if cearch in i:
#         print("нашли ОК",)
#         break
#     else:
#         for vtoroy in i:
#             print("2 уровнеь", vtoroy)
#             if cearch == vtoroy:
#                 print("нашли ОК")
#                 break
#             else:
#                 if type(vtoroy) is list:
#                     for tritiy in vtoroy:
#                         print(tritiy)
#                         if cearch == tritiy:
#                             print("нашли ок")
#                             break
#                         else:
#                             if type(tritiy) is list:
#                                 for chetv in tritiy:
#                                     print(chetv)
#                                     if cearch == chetv:
#                                         print("нашлт ок")
#                                         break
while True:
    chislo =int(input())
    if chislo > 0 and chislo !=7:
        print("положительное")
    elif chislo < 0:
        print("отрецательное")
    elif chislo == 0:
        print("ноль")
    elif chislo == 7:
        print("Goodbye")
        break
