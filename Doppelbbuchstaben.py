wörter = 0
wort = 0
def Doppelbuchstaben ():
    print ("Geben Sie ihre Wörter ein")
    wörter = input ()
    for wort in wörter:
        print(wort)
       # if wort == wort[]:
          #  print (wort)
    zahl = 0
    while zahl < len(wörter):
        if wörter[zahl] == wörter [zahl-1]:
            print("Buchstaben sind gleich")
        else: 
            print("Buchstaben sind ungleich")
       
       
        zahl += 1






Doppelbuchstaben ()

