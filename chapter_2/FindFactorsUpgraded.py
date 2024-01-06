import time


def FindFactors(number):
    factors = []

    #  проверяем делимость на 2
    while number % 2 == 0:
        factors.append(2)
        number //= 2

    # проверяем делимость на нечетные множители

    i = 3
    max_factor = number**0.5

    while i <= max_factor:
        #  проверяем делимость на i
        while number % i == 0:
            factors.append(i)

            number //= i

            #  устанавливаем новую верхнюю границу
            max_factor = number**0.5

        #  проверяем следующий нечетный множитель
        i += 2

    if number > 1:
        factors.append(number)
    
    return factors

start = time.time()
FindFactors(123456789)
end = time.time() - start
print("Время выполнения функции FindFactors", end)