# -*- coding: utf-8 -*-

""" ÖVNING:
    Skapa en lista med dictionaries, som ser ut så här:
    {
        "municipality": "Stockholm",
        "unemployment2014": 5.139667,
        "unemployment2013": 5.404515,
        "change": -0.264848,
        "sentence": "Din beskrivnade mening här...",
    }
    Det här motsvarar en rad i den kommande csv-filen som vi kommer att skapa
"""

import csv

# Öppnar filen
in_file = open("unemployment.csv", 'rb')
csv_file = csv.DictReader(in_file, delimiter=',')


def get_sentence(municipality, unemployment2014, unemployment2013):
    """Funktion för att beskriva abretslösheten"""
    sentence = "Arbetslösheten i %s var år 2014 %s procent jämfört med %s år 2013." % (municipality, unemployment2014, unemployment2013)
    return sentence

data = []
for line in csv_file:
    """ Övning
    """
    print line
