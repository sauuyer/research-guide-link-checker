from bs4 import BeautifulSoup
import requests
from requests.exceptions import Timeout
import pandas as pd

# this file gets and checks the links within one libguide specified by its url

# install appropriate packages
from bs4 import BeautifulSoup
import requests

#below, url is the chosen libguide that will be checked
research_guide_url = "https://guides.library.yale.edu/rdm_healthsci/"
response = requests.get(research_guide_url)
page_source = response.text
soup = BeautifulSoup(page_source, 'lxml')
sub_page_links_list = []
sub_page_links_list_clean = []

big_d = {}


def get_subpages():
    # get all subpages for the base-lib-guide
    css_subpage_soup = soup.find("ul", class_="nav nav-tabs split-button-nav")
    nav_links = css_subpage_soup.find_all('a')

    for a in nav_links:
        sub_page_links = a.get('href')
        sub_page_links_list.append(sub_page_links)


def clean_subpages():
    for i in sub_page_links_list:
        if i.startswith("https://guides.library.yale.edu/"):
            sub_page_links_list_clean.append(i)


def pull_subpage_links():
    for url in sub_page_links_list_clean:
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
                            big_d[href] = {"base_guide_url": research_guide_url, "guide_subpage_url": url, "http_status": r.status_code}
                    except Timeout:
                        big_d[href] = {"base_guide_url": research_guide_url,
                                                           "guide_subpage_url": url, "http_status": "timeout error"}


get_subpages()
clean_subpages()
pull_subpage_links()

df = pd.DataFrame.from_dict(big_d, orient='index')
pd.DataFrame.to_csv(df, "/Users/sn547/Documents/pycharm_projects/libguide-linkchecker/sample-output/output.csv")
print(list(df.columns))
print('done!')
