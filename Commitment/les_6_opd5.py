a = int(input("Voer de waarde van A in: "))
b = int(input("Voer de waarde van B in: "))
c = int(input("Voer de waarde van C in: "))

if a > b and a > c:
    print(f"Variabele A is het grootst, want {a} is groter dan {b} en {c}.")
elif b > a and b > c:
    print(f"Variabele B is het grootst, want {b} is groter dan {a} en {c}.")
elif c > a and c > b:
    print(f"Variabele C is het grootst, want {c} is groter dan {a} en {b}.")
else:
    print("De variabelen A, B en C zijn gelijk.")