def GCD(a, b):
    """Функция, возвращающая НОД двух чисел"""
    while b != 0:
        remainder = a % b
        # НОД(А, В) = НОД(В, остаток)
        a = b
        b = remainder

    return a


print(GCD(4851, 3003))
