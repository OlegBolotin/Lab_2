from random import sample

def numbrs():
    # создаём спиосок из рандомных чисел.
    numbers = sample(range(-10, 11), 5)

    # находим мин и макс значение в списке.
    x_min = int(min(numbers))
    x_max = int(max(numbers))

    # пробегаем список.
    for i in range(len(numbers)):
        # определяем чётность/не чётность и умножаем в зависемости результата.
        if int(numbers[i]) % 2 == 0:
            numbers[i] = int(numbers[i]) * x_min

        if int(numbers[i]) % 2 == 1:
            numbers[i] = int(numbers[i]) * x_max

    print(numbers)

numbrs()
