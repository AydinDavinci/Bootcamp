def multiply(a,b):
    keer = a * b
    return keer

print(multiply(5, 6))


def get_integer(prompt):
    nummer = int(input(prompt))
    return nummer

def get_float(prompt):
    nummer = float(input(prompt))
    return nummer

def get_string(prompt):
    string = input(prompt)
    return string

def get_letter(prompt):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter = input(prompt)
    while (not len(letter) == 1):
        print("invalid input ")
        letter = input(prompt)

    if letter in alphabet:
        letter = letter.upper()

    return letter


print(get_letter("voer een letter in"))