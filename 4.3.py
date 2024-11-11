import re
s = input()
j = 1
result = 0
operation = re.findall(r'[(\-/\+*)]', s)
print(operation)
numbers =re.split(r"[(\-/\+*)]", s)
while j < len(operation):
    # for x in numbers:
        for y in operation:
            if y == "+":
                result =numbers[j-1] +numbers[j]
        j += 1
print(result)

c
