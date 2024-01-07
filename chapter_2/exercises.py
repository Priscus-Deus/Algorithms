from random import choice

def imit_coin():
    """Напишите алгоритм, в котором игральная кость будет генерировать подбрасывания монеты."""
    edge = list(range(1,7))
    coin = choice(edge)
    if coin in {1,2,3}:
        return 'Орел'
    return 'Решка'

for i in range(10):
    print(imit_coin())