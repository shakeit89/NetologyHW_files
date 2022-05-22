# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }
# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
from pprint import pprint

cook_book = {}
with open('recipe.txt') as recipe_file:
    for line in recipe_file:
        cook = line.strip()
        count = int(recipe_file.readline())
        cook_book[cook] = []
        for i in range(count):
            data = recipe_file.readline().strip()
            data = data.split('|')
            cook_book[cook].append({'ingredient_name': data[0], 'quantity': data[1], 'measure': data[2]})
        recipe_file.readline()


def get_shop_list_by_dishes(dishes, person_count, book):
    order_dict = {}
    for dish, ingredients in book.items():
        for meal in dishes:
            meal = meal.capitalize()
            if dish == meal:
                for i in ingredients:
                    ingr_name = i['ingredient_name']
                    if ingr_name in order_dict.keys():
                        order_dict[ingr_name]['quantity'] += person_count * int(i['quantity'])
                    else:
                        order_dict[ingr_name] = {'measure': i['measure'], 'quantity': int(i['quantity']) * person_count}
    return order_dict


a = get_shop_list_by_dishes(['Омлет', 'фахитос'], 2, cook_book)
pprint(a)
