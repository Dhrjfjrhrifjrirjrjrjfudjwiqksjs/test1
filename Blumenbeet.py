beet = [7,2,4,7,3,6,5]
beetneu = [0]


def blumenbeet(beet):
    anzahl = 0 
    for b in beet:
        anzahl += b
    durchschnitt = anzahl /len(beet)
    
    print(durchschnitt)


blumenbeet(beet)


