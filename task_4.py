def task_4():
    lst_numbers = []

    user = int(input("Введите длину списка "))

    if user <= 4:
        print("В следующий раз введите больше 4-ох значений")
        exit()
    else: # заполняем список значениями.
        for i in range(user):
            a = int(input("Введите значения "))
            lst_numbers.append(a)

    print()
    print(lst_numbers)

    # приравниваем списки, удаляем макс и мин значения.
    lst_no_extremum = lst_numbers
    lst_no_extremum.remove(min(lst_no_extremum))
    lst_no_extremum.remove(max(lst_no_extremum))

    print(lst_no_extremum)


task_4()
