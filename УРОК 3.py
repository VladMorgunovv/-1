a = input("Введите число a: ")
b = input("Введите число b: ")
c = input("Введите число c: ")

string = a + b + c
print(string)


string = input()

result = int(string[0]) * int(string[1]) * int(string[2]) * int(string[3])

print(result)


metres = input("Введите метр")

print(f" {int(metres) * 100}")
print(f" {int(metres) * 10}")
print(f" {int(metres) * 1000}")
print(f" {int(metres) / 1609: .4f}")


triangle = input("Введите H и L: ")

h = float(triangle.split(" ")[0])
l = float(triangle.split(" ")[1])

print("Итого площадь треугольника равна: ", h*l/2)