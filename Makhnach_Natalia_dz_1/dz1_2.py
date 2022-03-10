my_list = []

for i in range (1, 1000, 2):
    my_list.append(i**3)


print(my_list)

#вычислите сумму тех чисел из списка, сумма цифр которых делиться нацело на 7

my_list_new = []


for i in my_list:
    if sum (map(int, str(i))) % 7 == 0:
        my_list_new.append(i)


print(my_list_new)

summ = 0
idx = 0
while idx < len (my_list_new):
    summ = summ + my_list_new[idx]
    idx = idx + 1

print(summ)


# к каждому элементу списка добавить 17
# и заново вычислить сумму тех чисел из этого списка сумма цифр которых делиться нацело на 7

my_list_new = []


for i in my_list:
    if sum (map(int, str(i+17))) % 7 == 0:
        my_list_new.append(i+17)


print(my_list_new)

summ = 0
idx = 0
while idx < len (my_list_new):
    summ = summ + my_list_new[idx]
    idx = idx + 1

print(summ)