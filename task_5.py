def task_5():
    # создаём словарь и 2 пустых списка
    sailor = {}
    team_1 = []
    team_2 = []

    value = int(input("Введите количество матросов: "))

    # заполняем словарь фамилиями и возрастом
    while len(sailor) + 1 <= value:
        username = input("Введите фамилию :")
        age = int(input("Введите возраст: "))
        sailor[username] = age

    # разделяем на команды по заданным условиям
    for i in sailor:
        if (sailor[i] > 20) and (sailor[i] < 40):
            team_2 += [i]
        else:
            team_1 += [i]

    # сортируем и выводим результат
    print("Команда 1: ", sorted(team_1))
    print("Команда 2: ", sorted(team_2))

task_5()
