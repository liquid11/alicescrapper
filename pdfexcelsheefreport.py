#!/usr/local/bin/python3
from bs4 import BeautifulSoup
import requests
import csv

sitemap_url = "https://www.aliceplatform.com/sitemap.xml"
sitemap = requests.get(sitemap_url)
sitemap_soup = BeautifulSoup(sitemap.content, "xml")
pages = sitemap_soup.find_all("loc")

with open('pdfanchors.csv', 'w', newline='\n') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    filewriter.writerow(['Page', 'URL', 'Achors in body section'])
    array_links = []
    for page in pages:

        url = page.get_text()
        page = requests.get(url)
        html = page.content
        soup = BeautifulSoup(html, 'html.parser')
        #data = soup.findAll('div', attrs={'class': 'body-container-wrapper'})
        page_title = soup.title.get_text()

        links = soup.find_all('a', href=True)
        for link in links:
            if "pdf" in link.get("href"):
                array_links.append(link.get("href"))

        filewriter.writerow([page_title, url, array_links])