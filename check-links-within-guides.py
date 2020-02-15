# this file gets and checks the links within one libguide

# install appropriate packages
from bs4 import BeautifulSoup
import requests

url = "https://guides.library.yale.edu/rdm_healthsci/"
response = requests.get(url)
page_source = response.text
soup = BeautifulSoup(page_source, 'lxml')

# Extracting all the <a> tags into a list.
css_soup = soup.find_all("div", class_="s-lg-guide-main")

main-div-class = "s-lg-guide-main"