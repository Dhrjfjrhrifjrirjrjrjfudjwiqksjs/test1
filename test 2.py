alter=24

if alter<=13:

    

    print("Du bist minderjährig.")
elif alter<18:
    print("Du bist ein Teenager.")
else:
    print("Du bist ein Erwachsener.")


    obst=["Apfel","Banane","Kirsche","Mango","Kiwi","Ananas","Orange","Wassermelone","Erdbeere","Honigmelone","Traube"]
    for x in obst:
        print(x)


i=1
while i<6:
    print(i)
    i+=1


Jahreszahlen=[2024,2025,2026,2027,2028,2029,2030,2031,1900,2000]
for x in Jahreszahlen:
    print(x)
    if x % 4==0:
        print("Das Jahr ist ein Schaltjahr.")
    elif x % 100==0:
        print("Das Jahr ist kein Schaltjahr")
    elif x % 400==0:
        print("Das Jahr ist ein Schaltjahr")
    else:
        print("Es ist kein Schaltjahr")

J=2000
while J>2000:
    print(J)
    

ungerade=[1,3,5,7,9]

x=1
while x< 11:
    if  x  % 2 == 0:
        print(x,"Es ist eine gerade Zahl")   
    else:
        print(x,"Es ist eine ungerade Zahl")       
    x+=1 



Zahlen=[143,55,82,2,66,8263,2,132,]
Max=0
for Zahl in Zahlen:
    if Zahl >Max:
        Max=Zahl
print(Max)

Anzahl=0
Wochentage=["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sonntag"]
for Wochentag in Wochentage:
    if Wochentag[0:1]=="S":
        print(Wochentag," ist kein Wochentag")
        Anzahl+=1
print(Anzahl)



def hello_world(name):
    print("Hello World "+name)

hello_world("Liam")


def calculate_sum(a, b):
    print(a + b)

calculate_sum(1, 2)

