#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Написать функция, вычисляющую среднее геометрическое своих аргументов а1,а2,…аn.
Если функции передается пустой список аргументов,то она должна возвращать значение None
"""


def geo(*args):
    if args:
        values = [float(arg) for arg in args]
        values.sort()
        a = 1
        n = len(values)
        for i in values:
            a = a * pow(i, (1 / n))
        return a

    else:
        return None


if __name__ == "__main__":
    print(geo(1, 2, 6, 24, 5))
