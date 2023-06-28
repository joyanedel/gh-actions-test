import math

def add(x: int, y: int) -> int:
    return x + y

def subtract(x: int, y: int) -> int:
    return x - y

def multiply(x: int, y: int) -> int:
    return x * y

def divide(x: int, y: int) -> float:
    return x / y

def power(x: int, y: int) -> int:
    return x ** y

def root(x: int, y: int) -> float:
    return x ** (1 / y)

def log(x: int, y: int) -> float:
    return math.log(x, y)

def factorial(x: int) -> int:
    return math.factorial(x)