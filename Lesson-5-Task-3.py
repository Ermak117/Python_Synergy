# Запрашиваем минимальную сумму инвестиций
investment = int(input("Минимальная сумма инвестиций - "))
# Запрашиваем какую сумму готов инвестировать каждый из инвесторов
Mike = int(input("Майкл готов инвестировать - "))
Ivan = int(input("Иван готов инвестировать - "))
# Проверяем условия и выводим результат
if Mike >= investment and Ivan >=investment :
    print(2) # Оба инвестора имеют минимальную сумму
elif Mike >= investment and Ivan < investment:
    print ("Mike")# Только Майк имеет минимальную сумму
elif Ivan >= investment and Mike < investment:
    print ("Ivan")# Только Иван имеет минимальную сумму
elif (Mike + Ivan)>= investment :
    print (1) # Если не могут по отдельности, но могут вместе 
else :
    print(0)# Если ни один не имеет минимальной суммы 