# this file gets and checks the links within one libguide

# install appropriate packages
from bs4 import BeautifulSoup
import requests

#below, url is the chosen libguide that will be checked
url = "https://guides.library.yale.edu/rdm_healthsci/"
response = requests.get(url)
page_source = response.text
soup = BeautifulSoup(page_source, 'lxml')

sub_page_links_list = []
sub_page_links_list_clean = []


def get_subpages():
    # get all subpages for the base-lib-guide
    css_subpage_soup = soup.find("ul", class_="nav nav-tabs split-button-nav")
    nav_links = css_subpage_soup.find_all('a')

    for a in nav_links:
        sub_page_links = a.get('href')
        sub_page_links_list.append(sub_page_links)


get_subpages()

for i in sub_page_links_list:
    if i != "javascript:void();":
        sub_page_links_list_clean.append(i)

for x in sub_page_links_list_clean:
    print(x)

