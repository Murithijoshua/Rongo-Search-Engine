import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
from totext import seperatingFiles
import logging
import time
from os import path
from linksep import separatelinks

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


# get all links inside <a> anchor tag
def links_home(link: str):
    html = urllib.request.urlopen(link).read()
    return (BeautifulSoup(html, "html.parser"))('a')


# get all text(link) inside href
def get_href(tags: list):
    return [tag.get('href') for tag in tags]


# since we do have first set of links we will go ahead to extract extra links inside the extracted links
def morelinks(link: str):
    return get_href(links_home(link))
# removing social media links


def find_social_link(link):
    socialLinks = ["google", "youtube", "twitter", "instagram", "linkedin"]
    return any(i in link for i in socialLinks)


# removing ID links
def cleaning_links(links: list):
    return [
        link
        for link in links
        if not ((link.startswith("#")) and find_social_link(link))
    ]


def savelinks(links: set):
    for i in links:
        try:
            seperatingFiles(i)
        except:
            print(f"this was not extracted successfully {i}")
            continue


def first_urls(link: str):
    start = time.process_time()
    total = get_href(links_home(link))
    # clean above extracted links
    total = set(cleaning_links(total))
    savelinks(total)
    print(time.process_time() - start)
    return total


def child_links(links: set):
    child_links = []
    for link in links:
        time.sleep(10)
        try:
            child_links.append(first_urls(link))
            log.info(f'{len(child_links)}')
        except:
            print(f'their is problem with {link}')
    return child_links


if __name__ == "__main__":
    homelinks = first_urls("https://www.rongovarsity.ac.ke/")
    secondary_links = child_links(homelinks)
