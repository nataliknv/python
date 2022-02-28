my_list = [57.80, 46.51, 97, 22.05, 34, 53.2, 9.22, 13.2, 74.93, 64.67]

end_list: str = ', '

for i, numb in enumerate(my_list):
    price = str(f'{float(numb):.2f}').split('.')
    if i == len(my_list) - 1:
        end_list = '\n'
    print(f'{price[0]} rub {price[1]} kop', end=end_list)

print(id(my_list))  # id до сортировки

my_list.sort()
print(my_list)
print(id(my_list))  # id после сортировки

new_list = my_list.copy()
new_list.sort(reverse=True)
print(new_list)

big_prises = new_list[0:4]
big_prises.sort()
print(big_prises)