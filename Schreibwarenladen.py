def Schreibwarenladen ():
    x = 0
    b = False 
    gesamt = 0
    while b == False :
        print ("Geben Sie das Produkt ein welches Sie kaufen möchten")
        c = input()
        print ("Geben Sie die Anzahl der Produkte ein")
        d = int(input ())
        if c == "Bleistift" : 
            gesamt = gesamt +d*0,5 
        elif c == "Heft" : 
            gesamt = gesamt + d*1
        else :
              None 
        print("Möchten Sie den Einkauf fortsetzen? ja/nein")
        e = input ()
        if e == "nein" : 
            break
        else:
            None
    print ("Danke für Ihren Einkauf. Ihr Gesamtbetrag beträgt:",gesamt,"Bezahlen Sie Bar oder mit Karte")
Schreibwarenladen()
