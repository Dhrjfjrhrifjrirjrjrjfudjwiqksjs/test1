summe = 0
import csv
count = 0
with open("/home/scts/Downloads/input_restaurant_bewertungen(1).csv") as csv_file:
    data = csv.reader(csv_file)
    next(data)
    for row in data:
  #      print(row)
        bewertungen = int(row[2])
        print(bewertungen)
        summe = summe + bewertungen
        print(summe)
        count = count +1
    print(summe / count) 


        