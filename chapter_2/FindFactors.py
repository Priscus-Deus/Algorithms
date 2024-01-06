import time

def FindFactors(number):
    factors = []
    i = 2

    while i < number:
        #  проверяем делимость на 2
        while number % i == 0:
            #  i является множителем, добавляем его в список
            factors.append(i)

            #  делим число на i
            number = number // 2

        # проверяем следующий возможный множитель
        i += 1

    #  Если от числа что-то осталось, то остаток тоже множитель

    if number > 1:
        factors.append(number)

    return factors

start = time.time()
FindFactors(123456789)
end = time.time() - start
print("Время выполнения функции FindFactors", end)
