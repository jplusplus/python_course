# -*- coding: utf-8 -*-
import csv

# Öppnar filen
in_file = open("unemployment.csv", 'rb')
csv_file = csv.DictReader(in_file, delimiter=';')

"""
 ÖVNING:
 Använd funktionen du skrev din hemuppgift och skriv en nyhet
 om arbetslösheten i varje kommun.
"""


def write_story(municipality, unemployment_2009, unemployment_2014):
    story = "Här kommer min nyhetstext om %s" % municipality
    # Skriv kod här!
    return story

# Loopa genom csv-filen
for row in csv_file:
    print("*****")
    print(row)

    # Gör om text till till decimaltal
    municipality = row["municipality"].decode("utf-8")
    unemployment_2009 = float(row["unemployment_2009"])
    unemployment_2014 = float(row["unemployment_2014"])

    # Anropa funktionen som skriver nyhetstexten
    story = write_story(municipality, unemployment_2009, unemployment_2014)

    print(story)
