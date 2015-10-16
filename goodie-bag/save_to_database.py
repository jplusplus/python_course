# coding: utf-8

"""
Dataset är ett smart bibliotek för att spara data i databaser i stället för csv-filer.
Databasen kan vara MySQL eller Postgres – koden är ändå densamma. Men allra enklast 
är det att skapa en SQLite-databas, som bara består av en lokal fil på din dator. Du
kan sedan använda programmet SQLitebrowser för att bläddra i databasen.

Läs mer om Dataset här: https://dataset.readthedocs.org/

Obs! Du måste köra "pip install dataset" i din terminal/kommandotolk för att det här
skriptet ska fungera första gången.
"""

import requests
import dataset
from bs4 import BeautifulSoup

""" 
Vi skapar automatiskt en ny SQLite-databas, om den inte redan existerar
"""
db = dataset.connect('sqlite:///blocket.db')

"""
Vi skapar en ny tabell ("products") i databasen, om den inte redan existerar
"""
table = db['products']

""" Funktionen öppnar en produktsida på Blocket och hämta varans namn och pris, samt url.
"""
def get_product_details(url):
    print("Öppnar %s" % url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text)

    product = {
        "name": soup.find("h1").text.strip(),
        "price": soup.find(id="vi_price").text.strip().replace(":-",""),
        "url": url # Det är ofta smart att också spara urlen till den sida man skrapat
    }

    return product

def save_to_db(row):
    """ 
    table.upsert är en smart funktion i Dataset som skapar en ny rad i databasen
    om den inte redan existerar. Annars uppdateras den befintliga raden. Detta är 
    användbart om man kör samma scraper flera gånger.
    ['url'] anger här de fält som fungerar som nycklar i databasen. Skriptet kommer att
    kolla om det finns nån befintlig rad med samma url.
    """
    table.upsert(row, ['url'])
    print ("Sparar produktdata för %s" % url)



url = "http://www.blocket.se/stockholm/Vit_garderob_63290080.htm?ca=11&w=1"
"""
Hämta produktdata
"""
product_details = get_product_details(url)

"""
Spara den i databasen
"""
save_to_db(product_details)

