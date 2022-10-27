#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Дано время забега на дистанцию 100 метров студентами в виде ключ-значения.
Определить лучшее время и среднее время среди всех студентов.
"""


def beg(**keywords):
    summa = 0
    n = len(keywords)
    min = keywords["Вася"]
    for kw in keywords:
        summa = summa + keywords[kw]
        if keywords[kw] < min:
            min = keywords[kw]
    print("Лучшее время:", min)
    print("Среднее время среди всех студентов - ", summa / n)


if __name__ == "__main__":
    beg(Вася=10.2,
        Виталик=11.3,
        Адам=10.1,
        Вова=9.98,
        Дина=12.3,
        )
