# coding: utf-8

"""
Ofta när man vill skrapa en sida med någon form av listning består navigationen av
en "nästa sida"-länk.
Här är ett exempel på ett skript som går vidare till nästa sida så länge det finns
en "nästa sida"-länk.
"""

import requests
from bs4 import BeautifulSoup
import re

base_url = "http://www.blocket.se/stockholm"
start_url = "http://www.blocket.se/stockholm?ca=11"


"""
Den här funktionen kollar om det finns någon nästa sida-länk.
Om det gör det returneras url:en till den, annars "False". 
"""
def has_next_page_link(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)

    """
    Viktigt steg!
    Här definierar jag hur skriptet ska söka efter en nästa sida-länk.
    I det här fallet letar vi efter länkar ("a") som innehåller texten "Nästa sida"
    """
    pattern = re.compile(u'Nästa sida')
    next_link = soup.find("a",text=pattern)

    if next_link:
        return base_url + next_link["href"]
    else:
        return False


def scrape_product_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    """ Skrapa produktsidan här!
    """

def scrape_product_list(url):
    print(u"Öppnar %s" % url)

    """
    Här skrapar du alla produktlänkar och öppnar dem en i taget.
    T.ex. med en funktion scrape_product_page()
    """

    """
    När alla produktsidor är skrpade kollar du om det finns en nästa sida-länk.
    """ 
    next_link = has_next_page_link(url)
    if (next_link):
        scrape(next_link)


scrape_list(start_url)