#  Используем метод Ньютона для нахождения корней функции f(x) 
from sympy import *


def dfdx(x):
    x = symbols('x')
    
    return diff(x ** 3 /5 - x ** 2 + x, x)


def func(x):

    y = x ** 3 /5 - x ** 2 + x

    return y

def find_zero(func, dfdx, initial_guess, max_error):

    x= initial_guess

    for i in range(100):
        y = func(x)

        if abs(y) < max_error:
            break

        x -= y / dfdx(x)

    return x

print(find_zero(func, dfdx, 3, 0.01))