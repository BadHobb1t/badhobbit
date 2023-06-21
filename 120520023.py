goods = [
    {
        'name': 'Iphone 14',
        'brand': 'Apple',
        'price': 1200
    },
    {
        'name': 'Iphone 11',
        'brand': 'Apple',
        'price': 400
    },
    {
        'name': 'Samsung Galaxy A23',
        'brand': 'Samsung',
        'price': 600
    },
    {
        'name': 'Xiaomi Mi13 Ultra',
        'brand': 'Xiaomi',
        'price': 800
    }
]

apple_list = filter(lambda item: item['brand']=='Apple', goods)
print(list(apple_list))
# for i in apple_list:
#     print(i)
# def item_price(item):
#     return item['price']

# print(sorted(goods, key=lambda item: item['price']))




goods = [
    {
        'name': 'Iphone 14',
        'brand': 'Apple',
        'price': 1200
    },
    {
        'name': 'Iphone 11',
        'brand': 'Apple',
        'price': 400
    },
    {
        'name': 'Samsung Galaxy A23',
        'brand': 'Samsung',
        'price': 600
    },
    {
        'name': 'Xiaomi Mi13 Ultra',
        'brand': 'Xiaomi',
        'price': 800
    }
]


# apple_list = filter(lambda item: item['brand']=='Apple' and item['price']>1000, goods)
# print(list(apple_list))
# for i in apple_list:
#     print(i)
# def item_price(item):
#     return item['price']

# print(sorted(goods, key=lambda item: item['price']))


# a = ['1', '2', '3', '4']
# b = map(int, a)
# print(list(b))

# def sss(item):
#     return item + 'sss'
#
# print(list(map(sss, a)))

# for i, item in enumerate(goods):
#     print(i, item)


# names = ['Артур', "Илья", "Стасян", "Денис"]
# surnames = ["Кочергин", "Лобанов", "Шикирюк", "Додолин"]
# favorite_object = ['Математику', "Информатика", "Изо", "Физ-ра"]
#
# for name, surname, object in zip(names, surnames, favorite_object):
#     print(name, surname, object)

# for item in zip([x['name'] for x in goods],[x['price'] for x in goods]):
#     print(item)
#

a = 'алексей'
print(a.capitalize())
