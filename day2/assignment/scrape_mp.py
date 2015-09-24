# -*- coding: utf-8 -*-

# STEG 1:
# Sätt upp en ny virtuell miljö och installera lxml.

import csv
import urllib2
import lxml # Eller beautifulsoup?


# Den här bjuder vi på
def scrape_profile_page(html):
    pass


def slugify(name):
    # STEG 2
    """
     Alla ledande MP-politiker har profilsidor med adresser baserade
     på deras namn. T.ex. http://www.mp.se/om/mats-dahlberg
     Den här funktionen skriver om namn ("Mats Dahlberg") till så
     kallade "slugs" ("mats-dahlberg"), med gemener och utan specialtecken.
     Använd funktionerna .replace() och .lower() för att göra detta.
    """
    # Skriv kod här!
    slug = name
    return slug


# STEG 3
# Öppna filen miljopartiet.csv, samt en ny fil som vi kommer att skriva till

# STEG 4
"""
    Loopa alla rader i filen miljopartiet.csv med csv.DictReader().
    Gör följande för varje politiker:
    - Skapa en url med hjälp av funktionen slugify(),
      t.ex. http://www.mp.se/om/mats-dahlberg
    - Öppna urlen läs html-innehållet på sidan
    - Skicka det här innehållet som en parameter
      till funktionen scrape_profile_page()
    - Funktionen kommer att returnera en dictionary som ser ut så här:
    {
        "name": "MATS DAHLBERG",
        "email": "mats.dahlberg@mp.se",
        "mobile": "0703-98 60 55",
        "description": "Ledamot Jokkmokks kommunfullmäktige, ledamot Miljöpartiets partistyrelse"
    }
    - Skriv den här informationen till en ny csv-fil
"""
