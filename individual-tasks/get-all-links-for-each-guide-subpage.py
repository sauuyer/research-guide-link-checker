from bs4 import BeautifulSoup
import requests
from requests.exceptions import Timeout
import pandas as pd

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
            href = a.get('href')
            href_cleaned = []
            if type(href) is str:
                if "guides.library.yale.edu" in href:
                    pass
                elif type(href) == 'NoneType':
                    pass
                elif "mailto:" in href:
                    pass
                else:
                    try:
                        r = requests.head(href, timeout=10)
                        if r.status_code == 200:
                            pass
                        else:
                            #print(href, 'AND THEN', url, 'AND THEN', a, 'AND THEN', r.status_code)
                            big_d[href] = {"base_guide_url": url, "guide_subpage_url": a, "http status": r.status_code}
                    except Timeout:
                        print(href, 'AND THEN', url, 'AND THEN', a, 'AND THEN', 'Timeout Error')
                        big_d[href] = {"base_guide_url": url, "guide_subpage_url": a, "http status": "tim"}


pull_subpage_links()

print(big_d)
df = pd.DataFrame.from_dict(big_d, orient='index')
print(df)
