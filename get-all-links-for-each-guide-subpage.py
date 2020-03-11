from bs4 import BeautifulSoup
import requests

all_nav_urls = ["https://guides.library.yale.edu/rdm_healthsci/home",
"https://guides.library.yale.edu/rdm_healthsci/policies",
"https://library.medicine.yale.edu/research-data/find-datasets/",
"https://library.medicine.yale.edu/research-data/find-datasets/data-repositories",
"https://guides.library.yale.edu/rdm_healthsci/dmps",
"https://guides.library.yale.edu/rdm_healthsci/best_practices",
"https://guides.library.yale.edu/rdm_healthsci/documentation",
"https://guides.library.yale.edu/rdm_healthsci/quality",
"https://guides.library.yale.edu/rdm_healthsci/file_names",
"https://guides.library.yale.edu/rdm_healthsci/versioning",
"https://guides.library.yale.edu/rdm_healthsci/metadata_schema",
"https://guides.library.yale.edu/rdm_healthsci/data_support"]

nav_urls = []
big_d = {}

#remove non libguide links from the header
for u in all_nav_urls:
    if u.startswith("https://guides.library.yale.edu/"):
        nav_urls.append(u)

'''
#pull the urls from one subpage test
url = urls[2]
response = requests.get(url)
page_source = response.text
soup = BeautifulSoup(page_source, 'lxml')
css_subpage_soup = soup.find("div", class_="container s-lib-main s-lib-side-borders")
nav_links = css_subpage_soup.find_all('a')
print(nav_links)
'''


def pull_subpage_links():
    for url in nav_urls:
        response = requests.get(url)
        page_source = response.text
        soup = BeautifulSoup(page_source, 'lxml')
        css_subpage_soup = soup.find('div', class_='container s-lib-main s-lib-side-borders')
        nav_links = css_subpage_soup.find_all('a')
        for a in nav_links:
            try:
                href = a.get('href')
                r = requests.head(href)
                print(url, 'AND THEN', href, 'AND THEN', r.status_code)
            except requests.ConnectionError:
                href = a.get('href')
                print(url, 'AND THEN', href, 'AND THEN', "WHAT WE'VE GOT HERE IS A FAILURE TO CONNECT")


pull_subpage_links()

