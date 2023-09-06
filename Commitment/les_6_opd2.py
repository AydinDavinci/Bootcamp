
a = int(input("Voer de waarde van A in: "))
b = int(input("Voer de waarde van B in: "))

if a > b:
    print(f"Variabele a is het grootst want {a} is groter dan {b}")
elif b > a:
    print(f"Variabele b is het grootst want {b} is groter dan {a}")
else:
    print(f"Variabele a en b zijn gelijk.")