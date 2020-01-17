from decorators import cache_decorator
import operator


def get_operator(op):
    return {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow,
    }[op]


@cache_decorator
def calculator(a, b, operation):
    return get_operator(operation)(a, b)


if __name__ == '__main__':
    supportedOperations = ('+', '-', '/', '*', '**')
    while True:
        try:
            a = int(input('Введите число 1: '))
            b = int(input('Введите число 2: '))
            break
        except ValueError:
            print('Число, а не какую-то фигню!')

    while True:
        operation = input('Введите операцию: ')
        if operation in supportedOperations:
            break
        else:
            print('Операция не поддерживается!')

    print('Результат: ', calculator(a, b, operation))

