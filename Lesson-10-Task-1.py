pets = {}  

for _ in range (1):  
    name = input("Кличка питомца: ")  
    vid = input("Вид животного: ")
    age = int(input("Возраст питомца: "))
    owner_name = input("Имя хозяина: ")
    # Сохраняем информацию о питомце в виде словаря
    pets[name] = {
        'вид': vid,
        'возраст': age,
        'хозяин': owner_name
    }
def age_animals(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif age % 10 in [2, 3, 4] and not (age % 100 in [12, 13, 14]):
        return "года"
    else:
        return "лет"

print(f'Это {vid} по кличке {name}. Возраст питомца: {age} {age_animals(age)}. Имя владельца:{owner_name}')