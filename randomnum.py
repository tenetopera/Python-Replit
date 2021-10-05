# Gération d'un nombre aléatoire
# donner des indication au fil de l'eau en fonction des propositions 
# au sujet du nombre que l'utilisateur essaie de deviner 

# pour utiliser la fonction importer la librarie random 

import random

_giranNum = random.randint(2,10)

# Boucle infinie
while True:
  _liuserRep = int(input ("Which number you think I've generated ? "))
  if (_liuserRep > _giranNum):
    print ("Too big ...")
  elif (_liuserRep < _giranNum):
    print ("Too small ...")
  else: 
    print ("Got it !")
# On sort de la boucle avec break
    break


