import random

def task_3():

    lst_random = []

    # вводим значени
    n = int(input())
    n_min = int(input())
    n_max = int(input())

    # заполняем список случайными числами из данного нам диапозона
    for i in range(n):
        a = random.uniform(-10, 10)
        lst_random.append(a)

    count = 0 # создаём счётчик

    # пробегаем список, вычисляем значения под наше условия, считаем кол-во
    for j in range(len(lst_random)):
        if int(lst_random[j]) >= n_min and int(lst_random[j]) < n_max:
            count = count + 1

    print(count)

task_3()
