# -*- coding: utf-8 -*-
import argparse


def get_parser():
    parser = argparse.ArgumentParser(description='Aufgabengenerator')
    parser.add_argument('min', type=int, help='Untere Grenze des Zahlenraums',
                        default=0)
    parser.add_argument('max', type=int, help='Obere Grenze des Zahlenraums',
                        default=1000)
    parser.add_argument('count', type=int, help='Anzahl der Aufgaben',
                        default=10)
    return parser
