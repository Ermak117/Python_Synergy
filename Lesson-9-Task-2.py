a = set(map(int, input('Введите числа в 1 список черезх пробел: ').split())) 
while len(a) > 100000:
    print('Ошибка! Список не должен превышать 100000 чисел')
    a = set(map(int, input('Введите числа в 1 список черезх пробел: ').split())) 

b = set(map(int, input('Введите числа во 2 список через пробел: ').split()))
while len(b) > 100000:
    print('Ошибка! Список не должен превышать 100000 чисел')
    b = set(map(int, input('Введите числа во 2 список через пробел: ').split()))
ab_numbers = a.intersection(b)
print (f'Одинаковых чисел в обоих списках : {len(ab_numbers)}')