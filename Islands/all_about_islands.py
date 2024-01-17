import math
import time
import timeit
from math import *


def fact_math(n):
    return sqrt(2 * pi * n) * (n / e) ** n * (1 + 1 / sqrt(52 * e * n))


def factorial(x):
    o = 1
    for i in range(1, x + 1):
        o = o * i
    return o


def factorial_rec(n):
    if n < 1:
        return 1
    else:
        num = n * factorial_rec(n - 1)
        return num


def mothik(x):
    return math.factorial(x)


numer = int(input("Введите значение numer "))
print("______________________________________________")

print(f"{fact_math(numer)}-результаты через формулу стирлинга")
print(f"Время использования функции: {timeit.timeit(lambda: fact_math(numer))}")
print(f"{fact_math(numer)/(mothik(numer)/100)-100} процентов - погрешность")
print("______________________________________________")

print(f"{factorial(numer)}-результаты через цикл")
print(f"Время использования функции: {timeit.timeit(lambda: factorial(numer))}")
print(f"{factorial(numer)/(mothik(numer)/100)-100} процентов - погрешность")
print("______________________________________________")

print(f"{factorial_rec(numer)}-результаты через рекурсию")
print(f"Время использования функции: {timeit.timeit(lambda: factorial_rec(numer))}")
print(f"{factorial_rec(numer)/(mothik(numer)/100)-100} процентов - погрешность")
print("______________________________________________")

print(f"{mothik(numer)}-результаты через библиотеку math")
print(f"Время использования функции: {timeit.timeit(lambda: mothik(numer))}")
print(f"{mothik(numer)/(mothik(numer)/100)-100} процентов - погрешность")
print("______________________________________________")
