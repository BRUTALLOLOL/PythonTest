

def repeat_three_times(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            print(i+1)
            func(*args, **kwargs)
    return wrapper

@repeat_three_times
def sum_of_squares(*args, **kwargs):
    result = 0

    # Позиционные аргументы
    for i in args:
        result += int(i) ** 2

    # Именованные аргументы
    for i in list(kwargs.items()):
        result += int(i[1]) ** 2

    print(result)


sum_of_squares(1, 2, 3,  a=1, b=3)

