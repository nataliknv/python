my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

len_list: int = len(my_list)

for i in range(len_list):
    x = my_list.pop(0)
    if x.isdigit():
        my_list.append(f'"{int(x):02d}"')
    elif x[0] =='+' and x[1].isdigit():
        my_list.append(f'"+{int(x):02d}"')
    else:
        my_list.append(x)


print(" ".join(map(str, my_list)))




