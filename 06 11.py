
import re
s =input()
# result =eval(s)
# print(result)
operation = re.findall(r'[(\-/\+*)]',s)
print(operation)
numbers =re.split(r'[(\-/\+*)]',s.replace(" ",''))
print(numbers)
i = 0
result = 0
res = []
j = 0
isk = []
while j < len(operation):
    print(operation[j])
    res =[]
    if operation[j] =="/":
            res.append(int(numbers[j]) / int(numbers[j+1]))
            isk.append(j)
            j = 0         
    if operation[j] =="*":
        res.append(int(numbers[j]) * int(numbers[j+1]))
        j = 0
    result +=res[0]
    j += 1
print(operation)