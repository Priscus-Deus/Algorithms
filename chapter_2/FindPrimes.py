#  находим простые числа между 2 и max_number (включительно)


def find_primes(max_number):
    is_composite = [False for i in range(max_number + 1)]

    for i in range(4, max_number + 1, 2):
        is_composite[i] = True

    next_prime = 3
    stop_at = max_number**0.5

    while next_prime <= stop_at:
        #  исключаем числа, кратные данному простому числу

        for i in range(next_prime * 2, max_number, next_prime):
            is_composite[i] = True

        #  переходим к следующему простому числу, пропуская четные числа
        next_prime = next_prime + 2

        while (next_prime <= max_number) and (is_composite[next_prime]):
            next_prime += 2

    # заносим простые числа в список

    primes = []

    for i in range(2, max_number + 1):
        if not is_composite[i]:
            primes.append(i)

    return primes


print(find_primes(110))
