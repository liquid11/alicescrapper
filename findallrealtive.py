#!/usr/local/bin/python3
from bs4 import BeautifulSoup
import requests
import csv
import urllib

sitemap_url = "https://www.aliceplatform.com/sitemap.xml"
sitemap = requests.get(sitemap_url)
sitemap_soup = BeautifulSoup(sitemap.content, "xml")
pages = sitemap_soup.find_all("loc")



def is_relative(url):
    return not bool(urlparse.urlparse(url).netloc)


for page in pages:
    url = page.get_text()
    page = requests.get(url)
    html = page.content
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.findAll('div', attrs={'class': 'body-container-wrapper'})
    page_title = soup.title.get_text()
    links = []

    with open(page_title +".csv", 'w', newline='\n') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        filewriter.writerow(['Page', 'URL', 'Achors in body section'])

        # for page in pages:

        # url = page.get_text()


        imagesElements = soup.find_all('img', href=is_relative)
        for img in imagesElements:
            src = img.get('src')
            if src is not None:
                filewriter.writerow([src + "\n"])


        for div in data:
            anchors = div.findAll('a')


            for a in anchors:
                anchor = a.get('href')

                if anchor is not None:
                    #links.append(anchor)
                    #if anchor.find("www.aliceplatform.com") > -1:
                    #links.append(anchor)
                    filewriter.writerow([anchor + "\n"])
