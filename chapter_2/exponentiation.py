def RaiseToPower(a, p):
    """Возводим число А в степень Р"""

    answer = 1
    count = 0
    p_list = []
    i = 1

    while i <= p:
        p_list.append(a**i)

        i *= 2

    for j in bin(p)[-1:1:-1]:
        if int(j):
            answer *= p_list[count]
            count += 1
        else:
            count += 1

    return answer
