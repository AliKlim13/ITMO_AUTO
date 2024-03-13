def task_1() -> None:
    al_int: int = 13
    al_float: float = 3.15
    al_str: str = 'Alice'
    al_list: list = [1, 2, 3, 7, 9]
    al_bool: bool = True

    print(type(al_int))
    print(type(al_str))
    print(type(al_float))
    print(type(al_bool))
    print(type(al_list))
task_1()


def task_2() -> None:
    a = [1, 2, 3, 5, 8, 13, 21]
    print(a[0:3])
    return a
task_2()

def task_3(number: int) -> int:
    ''''''
    return number ** 2
result = task_3(5)
print(result)

