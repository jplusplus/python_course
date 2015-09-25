# -*- coding: utf-8 -*-

# Uppgift:
#
# 1. Installera beautifulsoup:
#         pip install beautifulsoup
# 2. Skriv funktionen slugify() så att den gör vad den ska
# 3. Öppna filer miljopartiet.csv
# 4. Skapa en slug för varje rad
# 5. Gör en fullständig url för varje slug
# 6. Anropa funktionen scrape_profile_page() med adressen
# 7. Skriv resultatet till en csv-fil.
#    Använd den officiella dokumentationen:
#    https://docs.python.org/2/library/csv.html

import csv
import urllib2
import BeautifulSoup


# Den här bjuder vi på
def get_tag_content(soup, tag, attr):
    result = soup.find(tag, attr)
    if result is None:
        return ""
    else:
        return result.string


# Den här bjuder vi på
def scrape_profile_page(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup.BeautifulSoup(page.read())

    name = get_tag_content(soup, 'h1', {})
    email = get_tag_content(soup, 'a', {'class': "email"})
    mobil = get_tag_content(soup, 'a', {'class': "tel"})
    politician = {
        "name": name,
        "email": email,
        "mobile": mobil,
    }
    return politician


def slugify(name):
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
