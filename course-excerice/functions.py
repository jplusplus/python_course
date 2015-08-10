# -*- coding: utf-8 -*-
import requests
from lxml import html
import re
import dataset

BASE_URL = "http://moderat.se"
db = dataset.connect('sqlite:///moderater.db')
table = db['politicians']

def get_region_urls():
	# Öppna startsidan
	print "Open %s" % BASE_URL
	page = requests.get(BASE_URL)
	
	# Läs html
	tree = html.fromstring(page.text)

	# Skapa en tom lista där vi kommer att spara alla url:ar
	region_urls = []

	# Med den här xpath:en fångar vi upp regionlänkar i en lista
	# Vi loopar sedan listan 
	for a in tree.xpath("//div[@class='RegionChooser-list'][1]/ul/li[@class='RegionChooser-list-item']/a"):
		region_url = "%s%s" % (BASE_URL, a.attrib['href'])
		region_urls.append(region_url)

	return region_urls

def get_person_urls_from_list(region_url):
	url = "%s/foretradare" % region_url

	print "Open %s" % url
	page = requests.get(url)
	tree = html.fromstring(page.text)

	person_urls = []

	for a in tree.xpath("//h3[@class='SearchPage-rep-title']/a"):
		person_url = "%s%s" % (BASE_URL, a.attrib['href'])
		person_urls.append(person_url)

	return person_urls

def scrape_person_page(url):
	print "Open %s" % url
	page = requests.get(url)
	tree = html.fromstring(page.text)

	person = {}
	person['url'] = url
	person['name'] = tree.xpath("//section[@class='Bingo-content']/h1")[0].text
	person['title'] = tree.xpath("//section[@class='Bingo-content']/h2")[0].text
	person['description'] = tree.xpath("//section[@class='Bingo-content']/div[@class='Bingo-content-contentBottom']")[0].text_content()
	person['sidebar'] = tree.xpath("//aside[@class='Bingo-aside']")[0].text_content()
	emails = []

	all_text = "%s%s" % (person['description'], person['sidebar'])
	for email in get_emails(all_text):
		emails.append(email)

	person['email'] = ",".join(emails)
	
	return person

def get_next_page(url):
	print "Open %s" % url
	page = requests.get(url)
	tree = html.fromstring(page.text)
	next_link = tree.xpath("//li[@class='Pager-item Pager-item--next']/a")
	if len(next_link) > 0:
		return "%s%s" % (BASE_URL, next_link[0].attrib['href'])
	else:
		return None

def add_person_to_db(row):
	print "Add %s to database" % row['name']
	table.upsert(row, ['url'])

# Från https://gist.github.com/dideler/5219706
def get_emails(s):
	regex = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                    "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                    "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))
	return (email[0] for email in re.findall(regex, s) if not email[0].startswith('//'))


