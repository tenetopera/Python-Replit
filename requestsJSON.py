# Lecture d'un fihier JSON en utilisant le package requests

import requests

# requesting 

r=requests.get ("https://jsonplaceholder.typicode.com/todos")

#on extrait le texte de la réponse du serveur donc le JSON dans son intégralité
#print (r.text)
#print (r.json())

# parse the r.json  list
ct=0
for i in r.json():
  #print (i)
  if (i["completed"]):
    ct+=1
    print(i["userId"])

print ("")
print ( str(ct) +" / " + str(len(r.json())) )




