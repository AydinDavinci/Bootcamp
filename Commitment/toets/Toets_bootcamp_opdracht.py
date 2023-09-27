# #---| OPDRACHT 1 |---

#a: Visual studio code is handig omdat hij veel codeer talen kent, zo kan hij ook laten zien als code goed is geschreven en dat hij het erkent.
#b: Zodat docenten kunnen zien vanaf hun eigen pc, en zodat het veilig in de servers van github staat.

#---| OPDRACHT 2 |---
a = 5  # dit is een voorbeeld van het datatype: Integer (int)
b = 10.5# dit is een voorbeeld van het datatype: Float
c = "Hallo wereld" # dit is een voorbeeld van het datatype: String (str)

#---| OPDRACHT 3 |---
# Schrijf code die de waarden van a en b omwisselt. Gebruik daarvoor een extra variabele.
a = 5
b = 10
a,b = b,a
# voeg jouw code toe…
# Controleer met onderstaande code of de waarden correct zijn verwisseld
print(f"a = {a}, b = {b}") # Moet "a = 10 b = 5" printen

#---| OPDRACHT 4 |---
# Los de problemen op (zonder exception handling).
leeftijd = int(input("Hoe oud ben je?"))
print(f"Dan duurt het nog ongeveer {67 - leeftijd} jaar voordat je met pensioen mag!")
 # Is 18 ingevuld? Dan zie je op de terminal: Dan duurt het nog ongeveer 49 jaar voordat je met pensioen mag!

 #---| OPDRACHT 5 |---
  # Schrijf een functie die 3 getallen bij elkaar optelt en zorg ervoor
 # dat de uitkomst ervan wordt getoond in de print
getal1 = 200
getal2 = 5
getal3 = 12
antwoord = getal1 + getal2 +getal3# of de naam van je eigen functie.
print(f"De som van {getal1} + {getal2} + {getal3} = {antwoord}")

 #---| OPDRACHT 6 |---

  # Maak de volgende code af:# Je moet bijbetalen als je over je minuten of je GB's heen gaat en geen onbeperkt abonnement hebt.
AANTAL_GB = 20 # Aantal GB data in je bundel
AANTAL_MINUTEN = 200 # Aantal belminuten in je bundel
ONBEPERKT = False # test ook met True
aantal_minuten_gebeld = int(input("Hoeveel minuten heb je gebeld?"))
aantal_GB_internet = int(input("Hoeveel GB's heb je gebruikt?"))
if aantal_minuten_gebeld >= AANTAL_MINUTEN or aantal_GB_internet >= AANTAL_GB and ONBEPERKT == False:
     print("Let op: je moet bijbetalen!")
else:
     print("Niets aan de hand gebruik je mobiel lekker verder!") 

#---| OPDRACHT 7 |---
# Print onder elkaar de getallen 1-250 met max 2 regels code.

for i in range (1, 251):
   print (i)

#---| OPDRACHT 8 |---
# Gegeven is:

lijst_eten = ['appel', 'pannenkoek', 'kiwi', 'hamburger']

# a: print een eenvoudig menu met de volgende layout:

# Onze menukaart:
# appel
# pannenkoek
# kiwi
# hamburger 
print('Onze menukaart:')
for menu in lijst_eten:
  print(menu)

# b: Schrijf code die ervoor zorgt dat alleen het eten met de langste naam wordt geprint in de terminal. # Let op: je moet in de code eerst bepalen welk eten de langste naam heeft (en dus niet hardcoded 1 voor de index gebruiken). # test je code door extra eten toe te voegen met een nog langere naam.
lijst_eten = ['appel', 'pannenkoek', 'kiwi', 'hamburger']

#---| OPDRACHT 9 |---

cijfer_vraag = int(input('geef me een cijfer tussen 1-10: '))
ANTWOORD9 = 5

if cijfer_vraag != ANTWOORD9:
    print ("Helaas niet goed")

else:
    print ("Goed zo, dat is het juiste antwoord!")


# #---| OPDRACHT 10 |---
# repareer de volgende code:
MAX = 20
getal = print("Voer een getal in")
if getal > MAX:
    input(f"Het getal is groter dan {MAX}")
elif getal < MAX:
   input(f"Het getal is kleiner dan {MAX}")
else:
    input(f"Het getal is gelijk aan {MAX}")