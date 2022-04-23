import data
import random


# Funkcija nasumiscnog uzimanje pitanja iz baze "data.py"
def generisanje_objekata():
    broj = random.randint(0, len(data.data))
    objekat = data.data[broj]
    return f"{objekat['name']}, a {objekat['description']}, from {objekat['country']}.", int(objekat['follower_count'])


# Funkcija provere odgovora u zavisnosti od unosa
def uporedjivanje_pratioca(foloversi1, foloversi2, slovo):
    if slovo == "A":
        if foloversi1 > foloversi2:
            return foloversi1
        else:
            return False
    if slovo == "B":
        if foloversi1 < foloversi2:
            return foloversi2
        else:
            return False


# U promenljivu "takmicar1" se smesta funkcija "generisanje_objekata()"
takmicar1 = generisanje_objekata()
run = True
i = 0
print("\nDOBRO DOSLI U IGRU 'HIGHER LOWER'")


while run:
    # U promenljivu "takmicar2" se smesta funkcija "generisanje_objekata()"
    takmicar2 = generisanje_objekata()

    print(f"\n///////////////////////////////////////////////////////////////////////////////\nTRENUTNI SKOR = {i}")
    # Ispisivanje stringa koji se nalazi na prvom mestu u n-torci return-a funkcije "generisanje_objekata"
    print(f"\nCompare A: {takmicar1[0]}")
    print("VS")
    print(f"Compare B: {takmicar2[0]}")
    slovo = input("Ko ima vise foloversa? Upisi 'A' ili 'B': ")

    # Pozivanje funkcije "uporedjivanje_pratioca" radi provere tacnog unosa
    # Uzima se drugo mesto u n-torci return-a funkcije "generisanje_objekata"
    isTrue = uporedjivanje_pratioca(takmicar1[1], takmicar2[1], slovo)

    # U odnosu na return funkcije "uporedjivanje_pratioca", dodaje se poen i prelazi na vrh while petlje, ili
    # se izlazi iz igrice u slucaju netacnog odgovora
    if isTrue != False:
        if isTrue == takmicar1[1]:
            takmicar1 = takmicar1
            i += 1
            continue
        if isTrue == takmicar2[1]:
            takmicar1 = takmicar2
            i += 1
            continue
    else:
        print(f"Pogresan odgovor :( \n******* Vas konacni skor je {i} *******")
        run = False













