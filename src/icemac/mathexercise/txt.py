# -*- coding: utf-8 -*-
from .main import get_parser
from .model import generate_problems


def render(count, min, max):
    problems = generate_problems(count, min, max)
    print('Aufgaben')
    print('========')
    for i, p in enumerate(problems):
        print(p.render_problem())

    print('Lösungen')
    print('========')
    for i, p in enumerate(problems):
        print(p.render_problem(True))


def main():
    parser = get_parser()
    args = parser.parse_args()
    render(args.count, args.min, args.max)
