def Guten_Morgen(name):
    print("Guten Morgen"+name)

Guten_Morgen("Liam")

print("Enter your name:")
name = input()
print("Enter your age")
age = input()
print("Guten morgen" + name + age)
def check_age(age):
    if int(age) > 17:
        print("Du bist volljährig")
    elif int(age) < 18:
        print("Du bist minderjährig")

check_age(age)


i = 1
while i <= 5:
    print(i * i)
    i+=1




