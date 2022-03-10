def thesaurus(*names):
    scroll = {}

    for name in names:
        i = name[0]
        if i in scroll.keys():
            scroll[i].append(name)
        else:
            scroll[i] = [name]
    return scroll


print(thesaurus('Иван', 'Мария', 'Петр', 'Илья'))

