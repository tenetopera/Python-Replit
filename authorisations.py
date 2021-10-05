
# Declarations
username = ""
password = ""

retrycount = 0
retrylimit = 3

# Loop indefinitely 
while True:
# Test retry count and if the condition has been reached then pist them all off 
  if (retrycount>=retrylimit):
    print("The limit of "+str(retrylimit)+" has been reached. Pisted off !!!" )
    break
# Input 
  username = input ("username : ")
  password = input ("password : ")

# Embranchements
  if (username != "admin" and username != "pierre"):
    print ("unknown user ", username)
    retrycount+=1
  elif (password != "abc"):
    print("unauthorized user ", username)
    retrycount+=1
  else:
    print("Welcome on board ", username)
    break

