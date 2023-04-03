# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

# Сделано

month_number = int(input("Введите номер месяца: "))

if month_number == 1:
    print("Вы ввели январь. 31 день")
elif month_number == 2:
    print("Вы ввели февраль. 28 дней")
elif month_number == 3:
    print("Вы ввели март. 31 день")
else:
    print("Такого месяца нет!")
    
# Можно через словари кстати) 
m = int(input('Введите номер месяца и нажмите Enter: '))
months = {1:'январь, 31 день', 2:'февраль, 28 дней', 3:'март, 31 день', 4:'апрель, 30 дней', 5:'май, 31 день', 6:'июнь, 30 дней', 7 :'июль, 31 день', 8 : 'август, 31 день', 9 :'сенябрь, 30 дней', 10 :'октябрь, 31 день', 11 :'ноябрь, 30 дней', 12 :'декабрь, 31 день'}

if m in months:
    print(f"Вы ввели {months[m]}")
else:
    print('Такого месяца нет!')
