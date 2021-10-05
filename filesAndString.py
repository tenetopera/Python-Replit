# écriture dans fichier 
# Sauvegarde 

f=open ("./data.log","r")

entries = f.readlines()

nbl = len(entries)
nbe = 0

for item in entries:
  if (len(item) < 32):
    continue
  if (item.split("] - ")[0].split(" : ")[1] == "ERROR"):
    nbe+=1
    print (item)

f.close()

print(str(nbe)+"/"+str(nbl))

