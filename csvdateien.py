import csv
temp = 0
count = 0
with open("/home/scts/Downloads/locations.csv") as csv_file:
    data = csv.reader(csv_file) 
    next(data)

    #for row in data:
    #    print(row)
    #    temp = temp + int (row[2])
    #    count = count + 1
    #x = temp / count 
    #print(x)

    highesttemp = 0
    stadt = ""
    location = 0
    for row in data:
        if int(row[2]) > highesttemp:
            stadt = row[0]
            highesttemp = int(row[2])
    print(highesttemp)
    print(stadt)

with open("/home/scts/Downloads/locations.csv") as csv_file:
    data = csv.reader(csv_file) 
    next(data)

    lowesttemp = 50
    city = ""
    for row in data:
        if int(row[4]) < lowesttemp:
            city = row[0]
            lowesttemp = int(row[4])
    print(lowesttemp)
    print(city)

with open("/home/scts/Downloads/locations.csv") as csv_file:
    data = csv.reader(csv_file) 
    next(data)

    count = 0
    mindesttemp = 10
    for row in data:
        if int(row[4]) >= mindesttemp:
            count = count +1
    print(count)

with open("/home/scts/Downloads/locations.csv") as csv_file:
    data = csv.reader(csv_file) 
    next(data)

    liste = []
    for row in data:
        liste.append(row[0])
        liste.sort()
    print(liste)

with open("/home/scts/Downloads/klasse_8a.csv") as csv_file:
    data = csv.reader(csv_file) 
    next(data)

    note = 0
    count = 0
    for row in data:
        count row(2)







    
        



    


