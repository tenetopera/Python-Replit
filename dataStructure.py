# Gération d'un nombre aléatoire
# donner des indication au fil de l'eau en fonction des propositions 
# au sujet du nombre que l'utilisateur essaie de deviner 

# pour utiliser la fonction importer la librarie random 

#import dataStructure.py
#import intro.py
#import randomnum.py
#import loops.py
#import authorisations.py
#import requestsJSON.PY
#import files.py
#import filesAndJSON.py
#import JSONAndfiles.py
#import filesAndString.py
#import httpSourceParsing.py
#import httpSourceParsing2.py



# Lists and matrix

matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]
]

print("matrix = ")
for row in matrix:
  print(row)

#transposing matrix using nested list comprehension

print("matrixT=[[row[i] for row in matrix] for i in range (4)]")
matrixT=[[row[i] for row in matrix] for i in range (4)]

print("matrixT = ")
for row in matrixT:
  print(row)

#Tuples Packeing

T=123,23,2333,6566,"salut du con!",("sans oublier les sous-cons", "il y en a vraiment beaucoup",("parfois même trop", 1298723),["mais","il y en a qui peuvent quand même changer"])

print ("T = ",T)

#Tuples Unpacking
a,b,c,d,e,f = T
print ("a,b,c,d,e,f = T")

print("a = ",a)
print("b = ",b)
print("c = ",c)
print("d = ",d)
print("e = ",e)
print("f = ",a)

#Sets

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print ("basket = ",basket)

print ("'orange' in basket = ","orange" in basket)
print ("'crabgrass' in basket = ","crabgrass" in basket)

print("a = set('abracadabra')")
a = set('abracadabra')

b = set('alacazam')
print("b = set('alacazam')")

print ("a = ", a) 
print ("b = ", b)

print ("a - b = ", a - b)
print ("a | b = ", a | b)
print ("a & b = ", a & b)
print ("a ^ b = ", a ^ b)

# Sets comprehension

print ("a = {x for x in 'abracadabra' if x not in 'abc'}")
a = {x for x in 'abracadabra' if x not in 'abc'}
print ("a = ", a)

#Dictionaries

tel = {'jack': 4098, 'sape': 4139}
print ("tel = {'jack': 4098, 'sape': 4139}")
tel['guido'] = 4127
print("tel['guido'] = 4127")
print (tel)
print ("tel[\"jack\"] = ",tel["jack"])
del tel['sape']
print ("del tel['sape']")
tel['irv'] = 4127
print("tel['irv'] = 4127")
print("tel = ", tel)
print ("list (tel) = ", list(tel))
print ("sort (tel) = ", sorted(tel))
print ("guidi in tel = ", "guido" in tel)
print ("jack not in tel = ", "jack" not in tel)

#constructing dictonary from list of tuples 

mydic = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print("mydic = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])")
print("mydic = ", mydic)

#dictionary comprehension

mydic = {str(x) : x**2 for x in range (6)}
print("mydic = {str(x) : x**2 for x in range (6)}")
print ("mydic = ", mydic)

#Looping techniques

#for dictionary
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
print("knights = {'gallahad': 'the pure', 'robin': 'the brave'}")
for k, v in knights.items():
  print(k, v)

#for lists
mylist = ['tic', 'tac', 'toe']
print("mylist = ['tic', 'tac', 'toe']")

for i, v in enumerate (mylist):
  print(i,v)

#2 or more lists in thesame time with zip
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
print("questions = ['name', 'quest', 'favorite color']")
print("answers = ['lancelot', 'the holy grail', 'blue']")
for q, a in zip(questions, answers):
  print('What is your {0}?  It is {1}.'.format(q, a))
  



