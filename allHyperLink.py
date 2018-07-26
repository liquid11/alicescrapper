#!/usr/local/bin/python3
from bs4 import BeautifulSoup
import requests
import csv

sitemap_url = "https://www.aliceplatform.com/sitemap.xml"
sitemap = requests.get(sitemap_url)
sitemap_soup = BeautifulSoup(sitemap.content, "xml")
pages = sitemap_soup.find_all("loc")




with open('anchors.csv', 'w', newline='\n') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    filewriter.writerow(['Page', 'URL', 'Achors in body section'])

    for page in pages:

        url = page.get_text()
        page = requests.get(url)   
        html = page.content
        soup = BeautifulSoup(html,'html.parser')
        data = soup.findAll('div',attrs={'class':'body-container-wrapper'})
        page_title = soup.title.get_text()


        links = []
        for div in data:
            anchors = div.findAll('a')
            for a in anchors:
                anchor = a.get('href')

                if anchor is not None:
                    links.append(anchor)
                    #if anchor.find("www.aliceplatform.com") > -1:
                        #links.append(anchor)
            
            filewriter.writerow([page_title, url, links])