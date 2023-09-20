while True:
    vraag = int(input("Raad het getal...(alleen integers gebruiken)"))


    if vraag == 4:
        print("\033[92mJe hebt het getal goed geraden!\033[0m")
        break
        

    else: 
        print("\033[91mJe hebt het getal niet goed geraden!\033[0m")