# https://docs.python.org/3/library/csv.html
# https://docs.python.org/3/library/datetime.html
# https://www.guru99.com/date-time-and-datetime-classes-in-python.html
# https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
# https://stackoverflow.com/questions/25591025/how-to-get-all-the-image-links-download-using-python

from bs4 import BeautifulSoup
from datetime import datetime
import requests
import re
import csv

url = "http://www.raagalahari.com/actress/13192/regina-cassandra-at-big-green-ganesha-2014.aspx"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
data = []
today = datetime.now()

links = [a['href'] for a in soup.find_all('a', href=re.compile('http.*\.jpg'))]
imgs = [img['src'] for img in soup.find_all('img', src=lambda x: x.endswith('.jpg'))]
links += imgs

#a | for testing | print
imglink_count = (len(links))
link_list = ("\n".join(links))

#b | remove out the <div> of name and get its value
title = soup.find('h1', attrs={'class': ''})
page_title = title.text.strip()

#c | open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([today, page_title, imglink_count, link_list])
