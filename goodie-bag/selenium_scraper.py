# coding: utf-8

"""
När webbsidor som innehåller mycket Javascript och formulär är man ibland
tvungen att använda biblioteket Selenium för att öppna webbsidor,
istället för Requests.

Selenium låter en simulera händelser i browsern - klick, knapptryckningar,
textinmatningar. Selenium kommer att öppna upp ett browserfönster så att du
själv kan se vad som händer.

Installation:
 pip install selenium
 pip install beautifulsoup4
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep

# Öppna ett nytt webbläsarfön
driver = webdriver.Firefox()

# Gå till Hemnet
driver.get("http://www.hemnet.se")

# Hitta input-fältet för områdessök
search_field = driver.find_element_by_css_selector("#locations-panes .input-field input")

# Skriv Hornstull
search_field.send_keys("Hornstull")

# Vänta en sekund på att dropdown-listan ska laddas
sleep(1)

# Tryck enter
search_field.send_keys(Keys.ENTER)

# Hitta input-fältet för nyckelord och skriv balkong
keyword_field = driver.find_element_by_css_selector("#search_keywords")
keyword_field.send_keys("Balkong")

# Sök!
search_field.submit()

"""
Du kan även kombinera Selenium med BeautifulSoup så att du när du hittat t.ex.
en produktsida som du vill skrapa går över till BS som läser data från den som
vi lärt oss tidigare.
"""
soup = BeautifulSoup(driver.page_source, "lxml")

# Stäng browserfönstret efter 10 sekunder
sleep(10)
driver.close()
