naam = input("Voer uw naam in...")
leeftijd = int(input("Voer uw naam in jaren in..."))

if leeftijd < 18:
    print (f'Beste {naam}, je bent nog geen 18. Alleen autorijden zit er dus niet in :-(')
else:
    print(f'Beste {naam}, je bent 18 of ouder en je mag dus alleen autorijden (met rijbewijs althans)')