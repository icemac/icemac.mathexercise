# -*- coding: utf-8 -*-
import random
import operator


class Operation:

    operator = NotImplemented
    symbol = NotImplemented

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compute(self):
        return self.operator(self.a, self.b)

    def validate(self, min, max):
        if self.compute() < min:
            return False
        if self.compute() > max:
            return False
        return True

    def render_problem(self, with_solution=False):
        format = '{} {} {} ='
        args = (self.a, self.symbol, self.b)
        if with_solution:
            format += ' {}'
            args += (self.compute(),)
        return format.format(*args)


class Plus(Operation):
    operator = operator.add
    symbol = '+'


class Minus(Operation):
    operator = operator.sub
    symbol = '-'


OPERATORS = (Plus, Minus)


def generate_problem(min, max):
    while True:
        a = random.randint(min, max)
        b = random.randint(min, max)
        operation = random.choice(OPERATORS)(a, b)
        if operation.validate(min, max):
            return operation


def generate_problems(count, min, max):
    return [generate_problem(min, max) for x in range(count)]
