my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
a=min(my_list)
b=max(my_list)
def tmp(a):
    if a < b + 1:
        print(a)
        tmp(a + 1)
tmp(a)
print("Конец списка")