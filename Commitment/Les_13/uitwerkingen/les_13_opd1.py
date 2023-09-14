kleuren = ( 'rood' , 'blauw' , "groen" , 'paars' , 'oranje' , 'geel')

name = input('Wat is je naam?')
kleur = input('Wat is je favoriete kleur?')

if kleur in kleuren:
    print (f'Oke {name}, dus je favoriete kleur is {kleur}.')

else:
    print ('Deze kleur is niet zo geweldig!')