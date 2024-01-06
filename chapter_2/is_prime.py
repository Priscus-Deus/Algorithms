from random import choice


def is_prime(p, max_tests):
    #  проводим проверку max_tests раз
    for test in range(1, max_tests):
        n = choice(range(1, p))
        if (n ** (p - 1)) % p != 1:
            return False

    # С вероятностью 1 / (2 ** max_tests) число не является простым
    return True


print(is_prime(37, 10))
