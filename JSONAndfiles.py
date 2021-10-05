# Lire un fichier texte sérialisable JSON

import json

f=open("./users.txt","r")

users = json.load(f)

f.close
print (users)

