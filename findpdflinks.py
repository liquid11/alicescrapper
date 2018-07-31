#!/usr/local/bin/python3
from bs4 import BeautifulSoup
import requests
import csv
import urllib

sitemap_url = "https://www.aliceplatform.com/sitemap.xml"
sitemap = requests.get(sitemap_url)
sitemap_soup = BeautifulSoup(sitemap.content, "xml")
pages = sitemap_soup.find_all("loc")



#def is_relative(url):
#return not bool(urllib.urlparse.urlparse(url).netloc)


for page in pages:
    url = page.get_text()
    page = requests.get(url)
    html = page.content
    soup = BeautifulSoup(html, 'html5lib')
    data = soup.findAll('div', attrs={'class': 'body-container-wrapper'})
    page_title = soup.title.get_text()
    links = []

    with open("pdflink/" +page_title + ".txt", 'w', newline='\n') as txtfile:
        filewriter = csv.writer(txtfile, delimiter=',')
        filewriter.writerow(['Page', 'URL', 'Achors in body section'])

        current_link = ''
        # for page in pages:
        links = soup.find_all('a', href=True)
        for link in links:
            if "pdf" in link.get("href"):

            #if link is not None:
                #current_link = link.get('href')
                #if current_link.endswith('pdf'):
                    filewriter.writerow([link.get("href") + "\n"])




#imagesElements = soup.find_all('img')
#for img in imagesElements:
#src = img.get('src')

#if img is not None:
#filewriter.writerow([str(img) + "\n"])


#for div in data:
#anchors = div.findAll('a')


#for a in anchors:
#anchor = a.get('href')
#if a is not None:
#links.append(anchor)
#if anchor.find("www.aliceplatform.com") > -1:
#links.append(anchor)
#if is_relative(src):
#filewriter.writerow([str(a) + "\n"])
