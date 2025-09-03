number=int(input("Введите целое число: "))
if (number == 0):
    print("Нулевое число")
elif (number < 0) and ((number % 2 == 0 )):
    print("Отрицательное чётное число")
elif (number < 0) and ((number % 2 != 0)):
    print("Отрицательное нечётное число")
elif(number > 0) and ((number % 2 == 0)):
    print ("Положительное чётное число")
else:
    print("Положительно нечётное число")