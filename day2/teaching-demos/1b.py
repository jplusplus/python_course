# coding: utf-8

import martinwriter
import csv

in_file = open("unemployment.csv")
data = csv.DictReader(in_file, delimiter=";")

for row in data:
    municipality = row["municipality"].decode("utf-8")
    unemployment_2009 = float(row["unemployment_2009"]) 
    unemployment_2014 = float(row["unemployment_2014"]) 
    print("***")
    martinwriter.write_story(municipality, unemployment_2009, unemployment_2014)
