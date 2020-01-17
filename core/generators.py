# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
import random


def gen(N):
    return list(random.randrange(1, 100) for _ in range(N))


# написать генераторное выражение, которое делает то же самое
N = int(input("Сколько генерировать?"))
generation_var = [random.randrange(1, 100) for _ in range(N)]
