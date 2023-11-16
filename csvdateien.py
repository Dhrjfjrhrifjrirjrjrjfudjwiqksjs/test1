import csv
temp = 0
count = 0
with open("/home/scts/Downloads/locations.csv") as csv_file:
    data = csv.reader(csv_file) 
    next(data)


    for row in data:
        print(row)
        temp = temp + int (row[2])
        count = count + 1
    x = temp / count 
    print(x)

    


