import csv
A = 5
B = 7
C = 3
D = 9
E = 6
gesamtsumme = 0
with open("/home/scts/Downloads/magischeRunen.csv") as csv_file:
    data = csv.reader(csv_file)
    for row in data:
        for element in row:
            for letter in element:
                if letter == "A":
                    gesamtsumme = gesamtsumme + 5
                elif letter == "B":
                    gesamtsumme = gesamtsumme + 7
                elif letter == "C":
                    gesamtsumme = gesamtsumme + 3
                elif letter == "D":
                    gesamtsumme = gesamtsumme + 9
                elif letter == "E":
                    gesamtsumme = gesamtsumme + 6
                print(gesamtsumme)


        
    
    