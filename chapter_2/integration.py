from math import sin


def slice_area(test_func, x1, x2, max_slice_error):
    #  Вычисляем значения на конечных и центральной точках
    y1 = test_func(x1)
    y2 = test_func(x2)
    xm = (x1 + x2) / 2
    ym = test_func(xm)

    #  Вычисляем площадь болльшой и двух меньших трапеций
    area12 = (x2 - x1) * (y1 + y2) / 2
    area1m = (xm - x1) * (y1 + ym) / 2
    aream2 = (x2 - xm) * (y2 + ym) / 2
    area1m2 = area1m + aream2

    # оцениваем насколько это близко
    error = (area1m2 - area12) / area12

    #  оцениваем погрешность
    if abs(error) < max_slice_error:
        return area1m2

    # Если погрешность слишком большая делим трапецию и пробуем еще раз
    return slice_area(test_func, x1, xm, max_slice_error) + slice_area(
        test_func, xm, x2, max_slice_error
    )


def test_func(x):
    y = 1 + x + sin(2 * x)

    return y


def use_rectangle_rule(test_func, xmin, xmax, num_intervals):
    #  вычисляем ширину прямоугольника
    dx = (xmax - xmin) / num_intervals

    #  добавляем площади прямоугольников

    total_area = 0
    x = xmin

    for i in range(1, num_intervals + 1):
        total_area = total_area + dx * test_func(x)
        x += dx

    return total_area


print(
    "Нахождение площади под графиком при помощи правила прямоугольников ->",
    use_rectangle_rule(test_func, 0, 5, 10),
)


def use_trapezoid_rule(test_func, xmin, xmax, num_intervals):
    #  вычисляем ширину трапеции
    dx = (xmax - xmin) / num_intervals

    #  добавляем площади трапеций

    total_area = 0
    x = xmin

    for i in range(1, num_intervals + 1):
        total_area = total_area + ((test_func(x) + test_func(x + dx)) / 2) * dx
        x += dx

    return total_area


print(
    "Нахождение площади под графиком при помощи правила трапеций ->",
    use_trapezoid_rule(test_func, 0, 5, 10),
)


def integrate_adaptive_midpoint(test_func, xmin, xmax, num_intervals, max_slice_error):
    #  Вычисляем ширину начальных трапеций
    dx = (xmax - xmin) / num_intervals

    #  Добавляем площади трапеций
    total_area = 0
    x = xmin
    for i in range(1, num_intervals + 1):
        #  добавляем кусочек области
        total_area += slice_area(test_func, x, x + dx, max_slice_error)
        x += dx

    return total_area


print(
    '"Нахождение площади под графиком при помощи адаптивной квадратуры ->',
    integrate_adaptive_midpoint(test_func, 0, 5, 2, 0.01),
)
