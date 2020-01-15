#!/usr/bin/python
# -*- coding: utf-8 -*-
import random;

# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100 (@PavelMeld включительно)
def gen(N):
    while N>0:
        yield(random.randint(1,100));
        N = N - 1

for x in gen(5):
    print(x);

# написать генераторное выражение, которое делает то же самое
print("Generator expression  : ");
for y in  (random.randint(1,100) for x in range(0, 5)):
    print(y);
