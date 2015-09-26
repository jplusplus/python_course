# -*- coding: utf-8 -*-
import csv

# Öppnar filen
in_file = open("unemployment.csv", 'rb')
csv_file = csv.DictReader(in_file, delimiter=';')

"""
 Övning:
 Gör om egenskaperna "unemployment_2009" och "unemployment_2014"
 från text till decimaltal med hjälp av float() och UTF-koda kommunens namn.
"""

# Loopa genom csv-filen
for row in csv_file:
    print("*****")
    print("Orignaldata:")
    print(row)

    # Skriv kod här!

    print("Korrekt formaterad data:")
    print(row)
