import urllib.request
from bs4 import BeautifulSoup
import time
import json

url = "https://old.reddit.com/top/"

request = urllib.request.Request(url)
html = urllib.request.urlopen(request).read()

soup = BeautifulSoup(html,'html.parser')

main_table = soup.find("div",attrs={'id':'siteTable'})
links = main_table.find_all("a",class_="title")

extracted_records = []
for link in links: 
    title = link.text
    url = link['href']
    #There are better ways to check if a URL is absolute in Python. For sake simplicity we'll just stick to .startwith method of a string 
    # https://stackoverflow.com/questions/8357098/how-can-i-check-if-a-url-is-absolute-using-python 
    if not url.startswith('http'):
        url = "https://reddit.com"+url 
    # You can join urls better using urlparse library of python. 
    # https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urljoin 
    record = {
        'title':title,
        'url':url
        }
    extracted_records.append(record)
    time.sleep(0.1)

with open('data.json', 'w') as outfile:
    json.dump(extracted_records, outfile)