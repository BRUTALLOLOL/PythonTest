def sum_of_squares(*args, **kwargs):
    result = 0

    # Позиционные аргументы
    for i in args:
        result += int(i) ** 2

    # Именованные аргументы
    for i in list(kwargs.items()):
        result += int(i[1]) ** 2

    return result


print(sum_of_squares(1, 2, 3, a=1, b=3))
