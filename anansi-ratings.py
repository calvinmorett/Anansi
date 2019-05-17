from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime

###################
# ex, for testing # 
# url = "https://www.rcq.gouv.qc.ca/RCQ212AfficherFicheTech.asp?intNoFilm=266572"
################### 

url = input("URL to Crawl for Titles, and Rating Images: ")
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

# Snag Page Title
film_title = soup.title.string

# Snag Both Film Title Languages nested in an H2
film_all_title = soup.find('h2', attrs={'class': 'titreFilmHolder'})

# Snag Film Rating - Rating in Alt + img filename.gif
rating_img = soup.find('img', attrs={'id': 'icone-classement'})

# data.append((title))
today = datetime.now()

imgsrc = ("https://www.rcq.gouv.qc.ca" + rating_img['src'])
rating_FR = (rating_img['alt'])
film_name = (film_all_title.text.strip())
print(" ")
print(" ")
print(" ")
print(film_name)
print(rating_FR)
print(imgsrc)
print(today)
print(" ")

# open a CSV file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([film_name, rating_FR, imgsrc, today])
