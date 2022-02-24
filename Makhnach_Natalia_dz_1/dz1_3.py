number = 1

i1=' процент'
i2=' процента'
i3=' процентов'

while number <=100:

    if number == 1 or number % 10 == 1 and number!= 11:
        print(number, i1)
    elif (number >=2 and number <=4) or (number%10 >=2 and number%10 <=4):
        print(number, i2)
    else:
        print(number, i3)

    number+=1
