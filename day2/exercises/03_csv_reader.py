# -*- coding: utf-8 -*-

import csv

in_file = open("unemployment.csv", "rb")
csv_file = csv.DictReader(in_file, delimiter=',')

""" STEG 1: Ta koden från föregående övning, men paketera den som en funktion som
	returnerar en mening om arbetslösheten.
"""
def write_sentence(municipality, unemployment2014, unemployment2013):
	# Skriv kod här!
	print("En dynamisk mening")

""" STEG 2:
	Loopa csv-filen och kör funktionen write_sentence() genom att ge den rätt parametrar. 
"""
for line in csv_file:
	# Skriv kod här!
	print(line)

