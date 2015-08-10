from functions import get_next_page, get_person_urls_from_list, get_region_urls, scrape_person_page, add_person_to_db

region_urls = get_region_urls()
for region_url in region_urls:
	person_urls = get_person_urls_from_list(region_url)
	
	for person_url in person_urls:
		person_data = scrape_person_page(person_url)
		add_person_to_db(person_data)

