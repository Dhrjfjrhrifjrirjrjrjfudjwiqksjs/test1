def count_words(a):
    count = 0
    for i in a:
        count = count + 1
    print(count)
    
words = ["Hallo","Welt","Ich","Bin","Es"]
count_words(words)



def extend_string(a):
    print(a + " mag ich gerne")

extend_string("Hähnchen Reis")



def find_greater(a,b):
    if a < b:
        print("Die Zahl " +str(b)+ " ist die größere von beiden")
    elif a > b:
        print("Die Zahl " +str(a)+ " ist die größere")
    else:
        print("Beide Zahlen sind identisch")


find_greater(33,45)


def calculate_average(liste):
    summe = 0
    count = 0
    for i in liste:
        summe = summe + i
        count = count + 1 
    average = summe / count 

    return average

zahlenfolge = [1,2,3,4,5]

print(calculate_average(zahlenfolge))
print(calculate_average([12,20,23,80,42]))