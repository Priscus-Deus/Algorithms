# импортируем функцию choice из модуля random для выбора псевдослучайного числа
from random import choice

# создаем массив чисел
array = list(range(10))

print(*array, "Массив до рандомизации")


def RandomizeArray(array):
    """Функция, рандомизирующая массив"""

    #  В списке for проходимся по каждому элементу массива
    for i in range(len(array) - 1):
        #  выбираем случайное число, которое будем использовать в качестве индекса, создав вместе с этим список индексов нашего массива
        j = choice([i for i in range(len(array))])
        # меняем местами значения величин
        array[i], array[j] = array[j], array[i]
    return array


print(*RandomizeArray(array), "Массив после рандомизации")
