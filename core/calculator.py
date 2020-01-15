#!/usr/bin/python
# -*- coding: utf-8 -*-
from decorators import cache_decorator
import sys

@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)

	if operation not in ("-","+","/","*","**"):
		raise NameError("Неизвестная операция {}".format(operation));

	return eval(str(a)+operation+str(b));


if __name__ == '__main__':
	try:
		a = int(input('Введите число: '))
	except ValueError:
		print("Неверное значение");
		sys.exit(1);

	try:
		b = int(input('Введите число: '))
	except ValueError:
		print("Неверное значение");
		sys.exit(1);

	operation = input('Введите операцию: ')

	try:
		print('Результат: ', calculator(a, b, operation))
	except NameError as e:
		dir(e);
		print("Ошибка : {}".format(e));
