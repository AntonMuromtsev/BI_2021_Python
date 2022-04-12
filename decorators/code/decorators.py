import time
import requests
import random
import math


# Task 1

def measure_time(func):
    def inner_function(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(end - start)

    return inner_function


@measure_time
def some_function(a, b, c, d, e=0, f=2, g="3"):
    time.sleep(a)
    time.sleep(b)
    time.sleep(c)
    time.sleep(d)
    time.sleep(e)
    time.sleep(f)
    return g


some_function(1, 2, 3, 4, e=5, f=6, g="99999")


# Task 2

def function_logging(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if len(args) == 0 and len(kwargs) == 0:
            print(f"Function {func.__name__} is called with no arguments")
        elif len(args) != 0 and len(kwargs) == 0:
            print(f"Function {func.__name__} is called with positional arguments:", args)
        elif len(args) == 0 and len(kwargs) != 0:
            print(f"Function {func.__name__} is called with keyword arguments:",
                  ', '.join(['{}={!r}'.format(k, v) for k, v in kwargs.items()]))
        else:
            print(f"Function {func.__name__} is called with positional arguments:", args, "and keyword arguments:",
                  ', '.join(['{}={!r}'.format(k, v) for k, v in kwargs.items()]))
        print(f"Function {func.__name__} returns output of type {type(result).__name__}")
        return result

    return inner


@function_logging
def func1():
    return set()


@function_logging
def func2(a, b, c):
    return (a + b) / c


@function_logging
def func3(a, b, c, d=4):
    return [a + b * c] * d


@function_logging
def func4(a=None, b=None):
    return {a: b}


print(func1(), end="\n\n")
print(func2(1, 2, 3), end="\n\n")
print(func3(1, 2, c=3, d=2), end="\n\n")
print(func4(a=None, b=float("-inf")), end="\n\n")


# Task 3

def russian_roulette_decorator(probability, return_value):
    def decorator(func):
        def inner(*args, **kwargs):
            responce = func(*args, **kwargs)
            if random.random() < probability:
                return return_value
            else:
                return responce

        return inner

    return decorator


@russian_roulette_decorator(probability=0.2, return_value="Ooops, your output has been stolen!")
def make_request(url):
    return requests.get(url)


for _ in range(10):
    print(make_request("https://google.com"))


# Task 4

class CustomStaticmethod:

    def __init__(self, decorated_method):
        self.decorated_method = decorated_method

    def __get__(self, instance, owner):
        return self.decorated_method


class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @CustomStaticmethod
    def circle_area(r):
        return r ** 2 * math.pi


p = Pizza(4, ['mozzarella', 'tomatoes'])
try:
    print(p.area())
except:
    print("Method cannot be used")
print(Pizza.circle_area(4))
