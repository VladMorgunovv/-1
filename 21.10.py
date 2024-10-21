string = input().split(" ")

even = 0
even_numbers = []
adds = 0
adds_numbers = []
ent9 = 0
ent9_numbers = []


for i in range(int(string[0]), int(string[1])):
    if i % 2 == 0:
        even +=0
        even_numbers.append(i)
    if i % 2 !=0:
        adds += 1
        adds_numbers.append(i)
    if i % 9 ==0:
        ent9 += 1
        ent9_numbers.append(i)
print("количество четный: ",even, "ср арф: ", sum(even_numbers) / even)
print("количество НЕчетный: ",adds, "ср арф: ", sum(adds_numbers) / adds)
print("количество  крат 9: ",ent9, "ср арф: ", sum(ent9_numbers) / ent9)
