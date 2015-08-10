# -*- coding: utf-8 -*-

"""	STEG 1: 
	Sätt upp en ny virtuell miljö och installera lxml.
"""

import csv
import urllib2
import lxml # Eller beautifulsoup?


# Den här bjuder vi på 
def scrape_profile_page(html):
	pass

""" STEG 2: 
	Alla ledande MP-politiker har profilsidor med adresser baserat på deras namn.
	T.ex. http://www.mp.se/om/mats-dahlberg
	Men vi behöver göra en funktion som skriver om namn ("Mats Dahlberg") till så
	kallade "slugs" ("mats-dahlberg"), med gemener och utan specialtecken.
	Använd funktionerna .replace() och .lower() för att göra detta.

	Replace fungerar så här:
	name = "Jens Finnäs"
	name.replace(" ", "-")
	=> "Jens-Finnäs"

	Man kan även rada flera replace efter varandra:
	name.replace(" ","-").replace("ä","a")
	=> "Jens-Finnas"

"""
def slugify(name):
	# Skriv kod här!
	slug = name
	return slug

""" STEG 3: Öppna filen miljopartiet.csv, samt en ny fil som vi kommer att skriva till
"""
# Skriv kod här!

"""	STEG 4: 
	Loopa filen miljopartiet.csv
	Skapa en url för varje politiker med hjälp av funktionen slugify()
	http://www.mp.se/om/mats-dahlberg
	Öppna urlen för varje och läs html-innehållet på sidan
	Skicka html-texten som en parameter till funktionen scrape_profile_page()
	Funktionen kommer att returnera en dictionary som ser ut så här:
	{
		"name": "MATS DAHLBERG",
		"email": "mats.dahlberg@mp.se",
		"mobile": "0703-98 60 55",
		"decription": "Ledamot Jokkmokks kommunfullmäktige, ledamot Miljöpartiets partistyrelse"
	}
	Skriv den här informationen till en ny csv-fil
"""
# Skriv kod här!
