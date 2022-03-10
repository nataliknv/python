def num_translate():
    nums = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }

    num = input('число на английском от 0 до 10: ')
    print('на русском: ', nums.get(num))

num_translate()







