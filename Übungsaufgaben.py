zahlen = [15, 7, 23, 4, 9, 11, 5, 21]
def find_max_min(zahlen):
    zahlen.sort()
    print (str(zahlen[0])+"min.")
    print (str(zahlen[7])+"max.")
find_max_min(zahlen)





gesamtzahlen = [-2, 0, 5, -7, 0, 10, -3, 0, 8]
def classify_numbers(gesamtzahlen):
    gesamtzahlen.sort()
    positive_zahlen = 0
    negative_zahlen = 0
    null = 0
    for z in gesamtzahlen:
        if z >0: 
                positive_zahlen +=1
        elif z <0:
             negative_zahlen +=1
        else:
             null +=1            
    return ("anzahl der zahlen","negativ:",negative_zahlen,"positiv:",positive_zahlen,"null:",null )            
print (classify_numbers(gesamtzahlen))
