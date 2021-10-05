# parsing hhtp source code from a requested URL
# 

import requests
from bs4 import BeautifulSoup

#URL = "https://www.societe.com/cgi-bin/liste?nom=A&dirig=&pre=&ape=&dep="

#htmldoc = requests.get(URL).text

html_doc ="""

<a href="/societe/basalpine-autocars-005450093.html" class="txt-no-underline">

<div class="resultat">


<p class="iconsearch"><i class="icon-commerical-building"></i></p>

<p>

<span class="Link">SARL BAS ALPINE D'AUTOCARS "S.B.A"</span><br />

Autres commerces de détail spécialisés divers (4778C)<br />

04800 GREOUX LES BAINS

</p>




<p class="chevron">></p>

</div>

</a>

<hr />


<a href="/societe/etablissements-a-porquet-005620091.html" class="txt-no-underline">

<div class="resultat">


<p class="iconsearch"><i class="icon-commerical-building"></i></p>

<p>

<span class="Link">ETABLISSEMENTS A PORQUET</span><br />

Fabrication d'autres articles de robinetterie (2814Z)<br />

80132 HAUTVILLERS OUVILLE

</p>




<p class="chevron">></p>

</div>

</a>

<hr />


<a href="/societe/chanel-et-andrieu-battages-005750187.html" class="txt-no-underline">

<div class="resultat">


<p class="iconsearch"><i class="icon-commerical-building"></i></p>

<p>

<span class="Link">SOCIETE DE BATTAGES ET DE MOTOCULTEURS A. CHANUEL & J. ANDRIEU</span><br />


04200 MISON

</p>




<p class="chevron">></p>

</div>

</a>

<hr />

"""

soup = BeautifulSoup (html_doc,'html.parser')

ml = []

for i in soup.find_all("div",class_="resultat"):
  ml.append(i.span.text.strip())

print (ml)

htmldoc=requests.post("https://www.sirene.fr/sirene/public/recherche", data={"recherche.raisonSociale":"SOCIETE DE BATTAGES", "recherche.excludeClosed":"true", "__checkbox_recherche.excludeClosed":"true"}).text

print ("")

print ("************************************************")

print("")

print(htmldoc)
