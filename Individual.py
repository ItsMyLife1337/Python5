#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Напишите функцию, принимающую произвольное количество аргументов, и возвращающую требуемое значение.
Если функции передается пустой список аргументов, то она должна возвращать значение None.
В процессе решения не использовать преобразования конструкции *args в список или иную структу-ру данных.
Произведение аргументов, расположенных между максимальным и минимальным аргументами.
"""


def proiz(*args):
    pmin = 0
    pmax = 0
    maxi = 0
    pr = 1
    if args:
        for i in args:
            if i > maxi:
                maxi = i
                pmax = args.index(i)

        min = args[0]
        for i in args:
            if i < min:
                min = i
                pmin = args.index(i)

        for i in args[pmin+1:pmax:]:
            pr *= i
        return 'Произведение=', pr

    else:
        return None


if __name__ == "__main__":
    print(proiz(100, 200, 5, 300, 15, 555, 500))
