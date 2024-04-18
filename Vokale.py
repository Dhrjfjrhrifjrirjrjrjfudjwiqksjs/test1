vokale = ["a","e","i","o","u"]
woerter = ["Apfel","Banane","Erdbeere","Orange"]

def Vokalzaehler(liste):
    vokale_anzahl = 0

    for i in liste:
    
        for buchstabe in i:
            buchstabe = buchstabe.lower()
            if buchstabe in vokale:
                vokale_anzahl = vokale_anzahl +1
    print(vokale_anzahl)


Vokalzaehler(woerter)