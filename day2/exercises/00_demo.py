# -*- coding: utf-8 -*-
import csv

# Öppnar filen
in_file = open("unemployment.csv", 'rb')
csv_file = csv.DictReader(in_file, delimiter=';')


total_unemployment_2009 = 5.9
total_unemployment_2014 = 8.0

diff_total = total_unemployment_2014 - total_unemployment_2009


def write_story(municipality, unemployment_2009, unemployment_2014):
    # Räkna ut förändringen i kommunen
    diff = unemployment_2014 - unemployment_2009

    # Om arbetslösheten ökar
    if unemployment_2014 > unemployment_2009:
        print("Arbetslösheten i %s har stigit sedan finanskrisen med %s procentenheter." % (municipality, abs(diff)))

        # Jämför med landets arbetslöshet
        if diff > diff_total:
            print("Den har dessutom ökat mer än i hela riket")

    # Om arbetslösheten sjunker
    if unemployment_2014 < unemployment_2009:
        print("Arbetslösheten i %s var har sjunkit med %s procentenheter." % (municipality, abs(diff)))

    # Om arbetslösheten är oförändrad
    if unemployment_2014 == unemployment_2009:
        print("Arbetslösheten i %s var exakt lika stor 2014 som 2009.")


"""
Skriv ut innehållet på varje rad
"""
for row in csv_file:
    # Gör om kolumnen för arbetslöshet från text till decimaltal
    row["unemployment_2014"] = float(row["unemployment_2014"])
    row["unemployment_2009"] = float(row["unemployment_2009"])

    print("*** FLASH från J++!!!")
    write_story(row["municipality"], row["unemployment_2009"], row["unemployment_2014"])
