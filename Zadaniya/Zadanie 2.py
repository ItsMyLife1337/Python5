#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Решить поставленную задачу: написать функцию,
вычисляющую среднее гармоническое своих аргументов.
Если функции передается пустой список аргументов,
то она должна возвращать значение None.
"""


def garmonic(*args):

    if args:
        values = [float(arg) for arg in args]
        n = len(values)
        a = 0
        for i in values:
            a = a + (1 / i)
        return n / a

    else:
        return None


if __name__ == "__main__":
    print(garmonic(1, 6, 2, 2, 21))
