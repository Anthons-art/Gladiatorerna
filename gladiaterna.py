#Skriva intro text
#Göra så att spelaren kan anfalla
#Göra så att motståndare kan anfalla
#Presentera vem som vann

import random
import time
import os

print("Välkommen till Mortis Ludi!\n")
print("Välj svårighetsgrad:\n1. Enkel\n2. Medel\n3. Svår")
svårighetsgrad = int(input("Skriv in ditt val (1, 2, 3): "))

if svårighetsgrad == 1:
    healthpoints = 100  
    fiende = 50 
elif svårighetsgrad == 2:
    healthpoints = 80 
    fiende = 60  
elif svårighetsgrad == 3:
    healthpoints = 60  
    fiende = 70
else:
    print("Ogiltigt val, standardinställning (Medel) används.")
    healthpoints = 80
    fiende = 60

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')

clear_terminal()
time.sleep(1)

# Intro
blod = int(input("Välj mängden blodbeskrivningar: skriv '1' för mindre blod och '2' för mer blod "))

if blod == 2:
    blod = True
    print("Beskrivningarna blir mindre blodiga ")
else:
    blod = False
    print("Beskrivningarna blir mer blodiga")

print("\nVälj ditt vapen:\n1. Svärd\n2. Yxa\n3. Spjut")
vapenval = int(input("Skriv in ditt val (1, 2, 3): "))

if vapenval == 1:
    vapen = "svärd"
    skicklighet = 0.75  
    skada = 20 
elif vapenval == 2:
    vapen = "yxa"
    skicklighet = 0.65  
    skada = 22  
elif vapenval == 3:
    vapen = "spjut"
    skicklighet = 0.7  
    skada = 21  
else:
    print("Ogiltigt val, du får svärd som standardvapen.")
    vapen = "svärd"
    skicklighet = 0.75
    skada = 20

clear_terminal()
time.sleep(1)

print("\nMortis Ludi\n" 
      "===========\n" 
      "Du är gladiatorn Lady Eater, nu ska du slåss mot gladiatorn Guts.\n" 
      "Ni befinner er i en stor romersk arena i Nicaragua omgivna av en förväntansfull publik.\n"
      f"Du är klädd enbart i ett par baggy jeans, Vlone shirt, ett par Jordan 1s, och du råkar vara\n6,4 meter lång med dreads och ditt vapen: {vapen}. "
      "Motståndaren har slim jeans och en polo tröja... han vill ha dina kläder.\n"
      "Han ser redo ut att anfalla dig, gör dig redo.\n\nTryck ner enter för att fortsätta...")

input("")
time.sleep(1)
clear_terminal()

lista = ["spark", "slag", "kast"]
strid = True

print("Guts börjar springa emot dig med en arg blick\n")


while strid:
    fiendeval = random.choice(lista)

    print(f"Du har {healthpoints} hälsopoäng kvar.")
    print(f"Guts har {fiende} hälsopoäng kvar.")

    val1 = input("Vilket väljer du, slag, spark, kast eller vapen? ").lower()

  
    if val1 == "vapen":
        print(f"Guts väljer {fiendeval}")
        if random.random() <= skicklighet: 
            print(f"Du använder vapnet: {vapen} och träffar Guts!")
            fiende -= skada
            if blod:
                print(f"Blod flyger när du träffar Guts med vapnet: {vapen}!")
            
        else:
            print(f"Du missar med vapnet: {vapen}.")
            if fiendeval == "slag" or fiendeval == "kast" or fiendeval == "spark":
                print(f"Guts använder {fiendeval} och slår bort ditt vapen och skadar dig samtidigt.")
                healthpoints -= 10
    else:
        print(f"Guts väljer {fiendeval}")

        if val1 == fiendeval:
            print("Ni båda missar och stirrar argt på varandra.")

        elif val1 == "slag" and fiendeval == "kast":
            if blod:
                print("Guts kastar dig ner i sanden och spräcker flera blodkärl i din kropp. Det flyter ut blod ur din mun.")
            else:
                print("Guts kastar dig i golvet.")
            healthpoints -= 13

        elif val1 == "slag" and fiendeval == "spark":
            if blod:
                print("Du slår en hård uppercut mot Guts innan han hinner sparka dig. Blod och tänder kastas ut ur hans mun.")
            else:
                print("Du slår Guts innan han hinner sparka dig.")
            fiende -= 13

        elif val1 == "spark" and fiendeval == "kast":
            if blod:
                print("Du sparkar Guts i ansiktet och hans skalle spricker.")
            else:
                print("Du sparkar ner Guts på marken.")
            fiende -= 15

        elif val1 == "spark" and fiendeval == "slag":
            if blod:
                print("Guts slår dig i ansiktet och slår ut dina tänder innan du hinner sparka.")
            else:
                print("Guts slår dig innan du hinner sparka.")
            healthpoints -= 13

        elif val1 == "kast" and fiendeval == "spark":
            if blod:
                print("Guts sparkar dig hårt i magen innan du hinner kasta honom... blod flyger ut från din mun.")
            else:
                print("Guts sparkar dig innan du hinner kasta honom.")
            healthpoints -= 15

        elif val1 == "kast" and fiendeval == "slag":
            if blod:
                print("Du kastar ner Guts i marken och blod flyger ut ur hans mun.")
            else:
                print("Du kastar ner Guts i marken innan han slår dig.")
            fiende -= 13

    if fiende <= 0 or healthpoints <= 0:
        strid = False


if fiende <= 0:
    print("Du vann striden, Yippie!")
else:
    print("Fienden vann striden.")


