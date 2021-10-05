# Lecture d'un fihier JSON en utilisant le package requests
# Sauvegarde dans un fichier du résultat 

import requests
import json

# requesting 

r=requests.get ("https://jsonplaceholder.typicode.com/todos")

#on extrait le texte de la réponse du serveur donc le JSON dans son intégralité
#print (r.text)
#print (r.json())

# parse the r.json  list
ct=0
maliste = []
with open ("./user_filtered.txt","w") as f:
  with open ("./users.txt","w") as f2:
    for i in r.json():
      if (not(i["completed"])):
        continue

      ct+=1

      stro = str(i["userId"])+"\t"+i["title"]+"\r\n" + str(i) + "\r\n"
      print(stro)
      f.write(stro)

      dmp = json.dumps(i,indent=4)
      print(dmp +"\n")

      maliste.append(i)

    json.dump(maliste,f2,indent=4)
    f2.close

print ("")
stro = str(ct) +" / " + str(len(r.json()))

with open ("./user_filtered.txt","a") as f:
  f.write(stro)
  f.write("\r\n")
  f.close()


