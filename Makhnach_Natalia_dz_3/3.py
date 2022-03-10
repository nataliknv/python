from random import choice, randrange

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']

def get_jokes():

    x = choice(nouns)  #случайный выбор из первого списка
    y = choice(adverbs)  #случайный выбор из второго списка
    z = choice(adjectives)   #случайный выбор из третьего списка
    joke = '{} {} {}'.format(x, y, z) #объединение случайно выбранных слов в одну строку
    print(joke)

get_jokes()

