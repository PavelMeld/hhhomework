#!/usr/bin/python
# -*- coding: utf-8 -*-
def cache_decorator(original_function):
    # Реализовать декоратор который кэширует результаты вызова функции (есть в лекции)
    # Применить для функции calculator (в calculator.py уже есть import функции cache_decorator)
    # Настоятельно прошу написать декоратор руками, а не копировать, т.к. важно запомнить как это работает
    # PavelMeld : https://www.python.org/dev/peps/pep-0318/
    cache = {};

    def new_function(*args):
        if args not in cache:
            cache[args] = original_function(*args);
        return cache[args];

    return new_function;
