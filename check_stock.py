import urllib.request
import json
import datetime
from bs4 import BeautifulSoup

url_to_check = "https://mechboards.co.uk/shop/parts/hs60-hotswap-pcb/"


def get_souped_data(url):
	with urllib.request.urlopen(url) as response:
		html_in = response.read()
	return BeautifulSoup(html_in, 'html.parser')


def get_parent_element(passed_soup):
	return json.loads(passed_soup.find('form', class_='variations_form')['data-product_variations'])


def search_json_for_variation(json_arr, variation):
	print("Checking for the " + variation + " variation")
	for item in json_arr:
		if item['attributes']['attribute_pa_layout'] == variation:
			stock_soup = BeautifulSoup(item['availability_html'], 'html.parser')
			if stock_soup.text.rstrip() == "Out of stock":
				print(":( Out of stock")
			else:
				print(":D It's in stock")
				print(stock_soup.text)


soup = get_souped_data(url_to_check)
returned_json = get_parent_element(soup)

# change variation_to_check to iso, hhkb, ansi
variation_to_check = 'iso' #iso, hhkb, ansi
search_json_for_variation(returned_json, variation_to_check)
