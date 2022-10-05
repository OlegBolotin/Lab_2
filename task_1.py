def words():
    # создаём список из случайных слов и пустой список.
    words = ['overload', 'bulbs', 'editor', 'company', 'disaster', 'odd']
    my_list = []

    # пробегаем циклом список words
    for element in range(len(words)):
        # считаем длину каждого слова и добавляем в список.
        a = (len(words[element]))
        my_list.append(a)

    # считаем сумму самого длинного и короткого слоава.
    result = max(my_list) + min(my_list)
    print(result)

words()
