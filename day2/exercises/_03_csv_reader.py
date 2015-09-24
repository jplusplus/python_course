# -*- coding: utf-8 -*-

import csv

in_file = open("unemployment.csv", "rb")
csv_file = csv.DictReader(in_file, delimiter=',')

""" Det här programmet ska göra samma sak som det förra.
    Återanvänd kod därifrån!
"""


def write_sentence(municipality, unemployment2014, unemployment2013):
    # Skriv kod här!
    print("En dynamisk mening")

for row in csv_file:
    """Skriv kod här!"""
