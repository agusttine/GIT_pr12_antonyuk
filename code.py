while True:
    print("Вы человек? 1- да, 2-нет")
    try:
        proverka = int(input())
    except ValueError:
        print("Нет такого варианта выбора! давайте ещё раз!")
        continue

    if proverka not in (1, 2):
        print("Нет такого варианта выбора! давайте ещё раз!")
        continue
    break

print("Вы прошли проверку и попали в калькулятор сложения двух чисел!!!")

print("Введите 1 число: ")
num1 = int(input())
print("Введите 2 число: ")
num2 = int(input())

res = num1 + num2
print(f"Ответ: {res}")