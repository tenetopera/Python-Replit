# écriture dans un fichier 
# Sauvegarde 


data = input ("Entrez une phrase : ")

# Ouverture d'un fichier 

with open ("./data.txt","a") as f:
  f.write(data)
  f.write("\r\n")

f.close()

