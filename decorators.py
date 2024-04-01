

from typing import Any


def my_decorator(func):
    def wrapper():
        print('Estou antes da função!')
        func()
        print('Estou depois da função!')
    return wrapper


@my_decorator
def my_function():
    print('Estou na função!')


my_function()


class MyClass:
    def __init__(self, func):
        self.func = func

    def __call__(self) -> Any:
        print('Estou antes da função!')
        self.func()
        pass


@MyClass
def second_function():
    print('Estou na função!')


second_function()
