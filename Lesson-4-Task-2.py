# Ввод пятизначного числа 
number = int(input("Введите целое пятизначное число:"))
# Извлечение цифр
ten_thousands = number // 10000 % 10  # Десятки тысяч
thousands = number // 1000 % 10  # Тысячи
hundreds = number // 100 % 10  # Сотни
tens = number // 10 % 10  # Десятки
units = number % 10  # Еденицы
# Печатаем результат 
print((tens**units)*hundreds / (ten_thousands -thousands))