print("Geben Sie ihre Namen ein")
x = input()

namen = x.split()
namen.sort()

längster_name = 0

for i in namen:
   print(i) 
   len(i)
   if len(i) > längster_name:
      längster_name = len(i)

print(längster_name)


