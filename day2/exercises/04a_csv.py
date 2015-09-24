# -*- coding: utf-8 -*-
import csv

# Öppnar filen
in_file = open("unemployment.csv", 'rb')
csv_file = csv.DictReader(in_file, delimiter=';')

"""
Övning: Räkna hur många rader vi har i vår csv-fil
"""
counter = 0
for row in csv_file:
    print("*****")
    print(row)
    # Skriv kod här!

print("Det fanns %s rader i filen!" % counter)
