import os
from pprint import pprint

file_names = []

for file_name in os.listdir("sorted"):
    with open(os.path.join("sorted", file_name), 'r', encoding='utf-8') as file_obj:
        file_names.append(file_name)
        # counter = 0
        # for line in file_obj:
        #     counter += 1
        #     values.append(line.strip())
        # data[counter] = values

print(file_names)

data = {}

for file_name in file_names:
    with open(file_name, 'r', encoding='utf-8') as file_obj:
        values = []
        values1 = []
        counter = 0
        for line in file_obj:
            counter += 1
            values1.append(line.strip())
        values.append(file_name)
        values.append(values1)
        data[str(counter)] = values

pprint(data)

x = sorted(data.items())
pprint(x)

file_name_4 = "4.txt"

with open(file_name_4, 'w', encoding='utf-8') as file_obj:
    for i in x:
        file_obj.write(f"{str(i[1][0])}\n")
        file_obj.write(f"{str(i[0])}\n")
        for line in i[1][1]:
            file_obj.write(f"{line}\n")
