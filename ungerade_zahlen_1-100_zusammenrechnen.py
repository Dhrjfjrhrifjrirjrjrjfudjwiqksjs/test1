def zahlenraum():
    print("Gib die kleinste Zahl deines Zahlenraums ein")
    x = int(input())
    print("Gib die größte Zahl deines Zahlenraums ein")
    y = int(input())
    positiv = 0
    while x < y :
        if x % 2 == 0:
            positiv = x + positiv 
        else:
            None
        x+=1
    print(positiv)
zahlenraum()
        
