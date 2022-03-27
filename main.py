import data
import random


def generisanje_objekata():
    broj = random.randint(0, len(data.data))
    objekat = data.data[broj]
    return f"{objekat['name']}, a {objekat['description']}, from {objekat['country']}.", int(objekat['follower_count'])


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


takmicar1 = generisanje_objekata()
run = True
i = 0
print("\nDOBRO DOSLI U IGRU 'HIGHER LOWER'")


while run:
    takmicar2 = generisanje_objekata()

    print(f"\n///////////////////////////////////////////////////////////////////////////////\nTRENUTNI SKOR = {i}")
    print(f"\nCompare A: {takmicar1[0]}")
    print("VS")
    print(f"Compare B: {takmicar2[0]}")
    slovo = input("Ko ima vise foloversa? Upisi 'A' ili 'B': ")

    isTrue = uporedjivanje_pratioca(takmicar1[1], takmicar2[1], slovo)

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













