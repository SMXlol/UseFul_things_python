import math
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
print(f"{fact_math(numer)-mothik(numer)}-погрешность")
print("______________________________________________")

print(f"{factorial(numer)}-результаты через цикл")
print(f"{factorial(numer)-mothik(numer)}-погрешность")
print("______________________________________________")

print(f"{factorial_rec(numer)}-результаты через рекурсию")
print(f"{factorial_rec(numer)-mothik(numer)}-погрешность")
print("______________________________________________")

print(f"{mothik(numer)}-результаты через библиотеку math")
print(f"{mothik(numer)-mothik(numer)}-погрешность")
print("______________________________________________")
