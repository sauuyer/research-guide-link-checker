# this file collects all of the libguide links from the medical library guide page

# install appropriate packages
from bs4 import BeautifulSoup
import requests

# list for all lib-guide urls
all_libguide_urls = []

# gather all links from the lib-guide landing page
url = "https://library.medicine.yale.edu/guides"
response = requests.get(url)
page_source = response.text
soup = BeautifulSoup(page_source, 'lxml')

# Extracting all the <a> tags into a list.
css_soup = soup.find_all("div", class_="block-inner clearfix")
guide_content_block = css_soup[3]

# Extracting all the <a> tags into a list.
tags = guide_content_block.find_all('a')
for tag in tags:
    links = tag.get('href')
    all_libguide_urls.append(links)

# Remove the last url from the all-urls list because it is a link to a list of all Yale libguides
all_libguide_urls.pop()

for libguide_url in all_libguide_urls:
    print(libguide_url)


