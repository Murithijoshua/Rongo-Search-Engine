import urllib.request, urllib.parse, urllib.error
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


# removing ID links
def cleaning_links(links: list):
    return [
        link
        for link in links
        if not ((link.startswith("#")) )
    ]


if __name__ == "__main__":
    if not path.exists("../links.txt"):
        # getting all the links from the main page
        total = get_href(links_home("https://www.rongovarsity.ac.ke/"))
        # clean to remove ll ID links
        total = set(cleaning_links(total))
        other_links = []
        # loop in each link generated from main page(total) to prodeuce additional links then save then inside other_links variable
        for link in total:
            time.sleep(5)
            try:
                other_links.append(', '.join(cleaning_links(get_href(links_home(link)))))
                print(other_links)
            except:
                print(f'their is problem with {link}')
        print(other_links)
        total_links = total.union(set(other_links))
        # saving the generated links inside txt file
        with open('../links.txt', 'w') as f:
            for line in total_links:
                f.write(line)
                f.write('\n')
    else:


        # getting data from links extracted and saving it into .txt file
        separatelinks()
        def webpage_to_txt(links: str):
            count = 0
            for url in links:
                print(url)
                # logging.info(f"Getting data from {count} out of {len(links)}")
                try:
                    separatingFiles(url)
                except:
                    logging.info(f"Error Getting data from {url}")
                    continue
                count += 1

        with open('../links.txt', 'r') as f:
            data = f.read()
            print(data)
            webpage_to_txt(data)
            f.close()
