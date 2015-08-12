# -*- coding: utf-8 -*-

import csv

file_name = "unemployment.csv"

print "Öppnar %s" % file_name
csv_file = csv.DictReader(open(file_name, 'rb'), delimiter=',')

""" STEG 1: Ta koden från föregående övning, men paketera den som en funktion som
	returnerar en mening om arbetslösheten.
"""
def write_sentence(municipality, unemployment2014, unemployment2013):
	# Skriv kod här!
	return "En dynamisk mening"

""" STEG 2:
	Loopa csv-filen och kör funktionen write_sentence() genom att ge den rätt parametrar. 
"""
for line in csv_file:
	# Skriv kod här!
	print line
