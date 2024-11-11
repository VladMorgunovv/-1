import json

with open("new_test_hw.json",'r ') as file:
    json_data = json.load(file)

def find_companies(data):
    companies = []
    if isinstance(data, list):
        for item in data:
            companies.append(item)
    elif isinstance(data, dict):
        if ("id") in data and "title" in data:
            companies.append((data["title"]), data)
            for value in data.values():
                companies.extend(find_companies(value))
result = find_companies(json_data)

print(result)

