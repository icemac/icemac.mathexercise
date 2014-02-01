# -*- coding: utf-8 -*-
import random
import operator
import argparse


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


class Plus(Operation):
    operator = operator.add
    symbol = '+'


class Minus(Operation):
    operator = operator.sub
    symbol = '-'


OPERATORS = (Plus, Minus)


def aufgabe(min, max):
    while True:
        a = random.randint(min, max)
        b = random.randint(min, max)
        operator = random.choice(OPERATORS)(a, b)
        if operator.validate(min, max):
            return (a, operator.symbol, b, operator.compute())


def aufgaben(count, min, max):
    aufgaben = [aufgabe(min, max) for x in range(count)]
    print('Aufgaben')
    print('========')
    for i, x in enumerate(aufgaben):
        print('{0}) {1} {2} {3} ='.format(i + 1, *x))

    print('Lösungen')
    print('========')
    for i, x in enumerate(aufgaben):
        print('{0}) {1} {2} {3} = {4}'.format(i + 1, *x))


def get_parser():
    parser = argparse.ArgumentParser(description='Aufgabengenerator')
    parser.add_argument('min', type=int, help='Untere Grenze des Zahlenraums',
                        default=0)
    parser.add_argument('max', type=int, help='Obere Grenze des Zahlenraums',
                        default=1000)
    parser.add_argument('count', type=int, help='Anzahl der Aufgaben',
                        default=10)
    return parser


def txt():
    parser = get_parser()
    args = parser.parse_args()
    aufgaben(args.count, args.min, args.max)
