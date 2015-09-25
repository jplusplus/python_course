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
    """ Returnerar innehållet i den första html-taggen, av typen tagg,
        och med attributen attr. En tom sträng om ingen tagg hittades
    """
    result = soup.find(tag, attr)
    if result is None:
        return ""
    else:
        return result.string


# Den här bjuder vi på
def scrape_profile_page(url):
    """ Returnerar ett objekt med data om en miljöpartist, given en
        URL till deras profilsida. Så här:
        {"name": "", "email": "", "mobile": "", "description: ""}
    """

    # Öppna webbsidan, och hämta HTML-koden
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup.BeautifulSoup(html)

    # Den korta beskrivningen ligger i en <p>-tagg, inne i en <div>-tagg,
    # så här: <div class="lead"><p>Kommunstyrelsens ordförande</p></div>
    intro = soup.find('div', {'class': "lead"})
    if intro is not None:
        description = intro.find('p').string
    else:
        description = ""

    # <h1>-taggen innehåller alltid personens namn
    name = get_tag_content(soup, 'h1', {})
    # E-postadressen, om den finns ligger i: <a class="email">
    email = get_tag_content(soup, 'a', {'class': "email"})
    # Mobilnumret, om det finns ligger i: <a class="tel">
    mobil = get_tag_content(soup, 'a', {'class': "tel"})

    politician = {
        "name": name,
        "email": email,
        "mobile": mobil,
        "description": description,
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
