# this file gets and checks the links within one libguide

# install appropriate packages
from bs4 import BeautifulSoup
import requests

url = "https://guides.library.yale.edu/rdm_healthsci/"
response = requests.get(url)
page_source = response.text
soup = BeautifulSoup(page_source, 'lxml')

sub_page_links_list = []
sub_page_links_list_clean = []

def test_function():
    # get all subpages for the base-lib-guide
    css_subpage_soup = soup.find("ul", class_="nav nav-tabs split-button-nav")
    nav_links = css_subpage_soup.find_all('a')

    for a in nav_links:
        sub_page_links = a.get('href')
        sub_page_links_list.append(sub_page_links)


test_function()

for i in sub_page_links_list:
    if i != "javascript:void();":
        sub_page_links_list_clean.append(i)

print(len(sub_page_links_list))
print(len(sub_page_links_list_clean))

'''
# Extracting all the <a> tags into a list.
css_soup = soup.find("div", class_="container s-lib-main s-lib-side-borders")

# Extracting all the <a> tags into a list.
tags = css_soup.find_all('a')
for tag in tags:
    links = tag.get('href')
    print(links)
'''