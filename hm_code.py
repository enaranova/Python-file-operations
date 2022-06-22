from unittest import result
from pprint import pprint

# путь к файлу иерархии. методы для работы с путями

import os

LOG_CATALOG_NAME = "files" # есть такой каталог (каталог мы должны создать сами)
LOG_FILE_NAME = "data_dz.txt" # есть такой файл
BASE_PATH = os.getcwd() # путь к текущему каталогу где щас находимся

# print(BASE_PATH)

full_path = os.path.join(BASE_PATH, LOG_CATALOG_NAME, LOG_FILE_NAME)
print(full_path)

with open(full_path, 'r', encoding='utf-8') as file_obj:
    cook_book = {}
    for line in file_obj:
        dish = line.strip()
        cook_book[dish] = []
        for item in range(int(file_obj.readline())):
            ingredients = file_obj.readline()
            ingredients_list = ingredients.split(sep=" | ")
            ingredients_dictionary = {}
            ingredients_dictionary['ingredient_name'] = ingredients_list[0]
            ingredients_dictionary['quantity'] = int(ingredients_list[1])
            ingredients_dictionary['measure'] = ingredients_list[2].strip()
            cook_book[dish].append(ingredients_dictionary)
        file_obj.readline()
    # pprint(cook_book)
    # dishes = ['Омлет', 'Запеченный картофель']
    # person_count = 2
    # result = {}
    # for i in dishes:
    #     if i in cook_book.keys():
    #         for x in cook_book[i]:
    #             x['quantity'] *= person_count
    #             # print(type(x))
    #             result[x['ingredient_name']] = {}
    #             result[x['ingredient_name']]['measure'] = x['measure']
    #             result[x['ingredient_name']]['quantity'] = x['quantity']
    # print(result)

    def get_shop_list_by_dishes(dishes, person_count):
        result = {}
        for i in dishes:
            if i in cook_book.keys():
                for x in cook_book[i]:
                    x['quantity'] *= person_count
                    # print(type(x))
                    result[x['ingredient_name']] = {}
                    result[x['ingredient_name']]['measure'] = x['measure']
                    result[x['ingredient_name']]['quantity'] = x['quantity']
        return result
    
    pprint(get_shop_list_by_dishes(['Утка по-пекински', 'Фахитос'], 5))