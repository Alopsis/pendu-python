import random

# décla des mots 
motsPotentiel = ["cybersecurite" , "cryptographie", "forensic" , "pentest"]
alphabet = "azertyuiopqsdfghjklmwxcvbn"
randomNumber = random.randint(0, len(motsPotentiel)-1)
clearWord = motsPotentiel[randomNumber]
hiddenWord = ["_"] * len(clearWord)
choix = []
step = 0 # Le nombre de proposition :)
while "_" in hiddenWord and step < 9:
    print("Voici le mot : \n " + "".join(hiddenWord) + "\n")
    proposition = input("Quelle lettre voulez-vous proposer ?")
    if len(proposition) == 0:
        print("Veuillez entrer une lettre.")
        continue
    proposition = proposition[0]
    if proposition in alphabet:
        print("Vous avez proposé la lettre : " + proposition)
        if proposition in clearWord and proposition not in choix:
            # nouvelle lettre dans le mot 
            for n in range(0,len(clearWord) , 1 ):
                if clearWord[n] == proposition:
                    hiddenWord[n] = proposition
            step = step + 1 
            choix.append(proposition)
        elif proposition in choix:
            print("La lettre a déja été proposé")
        else:
            print("La lettre n'est pas dans le mot ")
            step = step + 1
            choix.append(proposition)
    else:
        print("La proposition est invalide ")
if "_" in hiddenWord or step >= 9:
    print("Vous avez perdu :( le mot était " + clearWord)
else:
    print("Bien joué ! vous avez trouvé le mot")