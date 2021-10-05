# parsing hhtp source code from a requested URL
# 

import requests
#from bs4 import BeautifulSoup

URL = "https://covid19.apple.com/mobility"

htmldoc = requests.get(URL).text

with open ("./covid.htm","a") as f:
  f.write(htmldoc)

f.close()


#soup = BeautifulSoup (htmldoc,'html.parser')

#for i in soup.find_all("h3",class_="acctext--con grid-item__title h4alt"):
  #print (i.text.strip())


