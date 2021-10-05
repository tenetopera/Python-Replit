# parsing hhtp source code from a requested URL
# 

import requests
from bs4 import BeautifulSoup

URL = "https://www.whitehouse.gov/about-the-white-house/presidents/"

htmldoc = requests.get(URL).text

soup = BeautifulSoup (htmldoc,'html.parser')

for i in soup.find_all("h3",class_="acctext--con grid-item__title h4alt"):
  print (i.text.strip())


