# -*- coding: utf-8 -*-
from .main import get_parser
from .model import generate_problems


def render(count, min, max):
    problems = generate_problems(count, min, max)
    render_block('Aufgaben', problems, False)
    render_block('Lösungen', problems, True)


def render_block(text, problems, show_solution):
    print(text)
    print('=' * len(text))
    for i, p in enumerate(problems):
        print('{}) {}'. format(i+1, p.render(show_solution)))


def main():
    parser = get_parser()
    args = parser.parse_args()
    render(args.count, args.min, args.max)
