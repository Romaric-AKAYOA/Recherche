ditionnaire ={}
#tuple =(1,2,4,5, "Bonjour", 'papa')
liste=[1,12.2,32,0,53,21]
tuple1 =(liste)
#print (ditionnaire )
dictionnaire={}
#ditionnaire["Nom"]="Romaric AKAYOA"
ditionnaire["Ecole"]="Lionil"
#val1= ditionnaire["Nom"]
#val2= ditionnaire.get("prenom")
for i in range(0,3):
    key=input("Donner la clé   ")
    val=input("donner une valeur  ")
    dictionnaire.update({key : val})

#for key in dictionnaire:
  #  print(key, " ", dictionnaire.get(key))
copy_dictionnaire={}
for key, value in dictionnaire.items():
    print("Pol/Eng ->", key, ":", value)
    copy_dictionnaire=dictionnaire.copy()

print(copy_dictionnaire)
 

#print(dictionnaire1)
#print(val1, "  ", val2)