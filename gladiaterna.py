#Skriva intro text
#Göra så att spelaren kan anfalla
#Göra så att motståndare kan anfalla
#Presentera vem som vann

import random
import time
import os

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def välj_svårighetsgrad():
    print("Välkommen till Mortis Ludi!\n")
    print("Välj svårighetsgrad:\n1. Enkel\n2. Medel\n3. Svår")
    val = int(input("Skriv in ditt val (1, 2, 3): "))
    if val == 1:
        return 100, 50  
    elif val == 2:
        return 80, 60
    elif val == 3:
        return 60, 70
    else:
        print("Ogiltigt val, standardinställning (Medel) används.")
        return 80, 60

def välj_blodnivå():
    blod = input("Välj mängden blodbeskrivningar: skriv '1' för mindre blod och '2' för mer blod ")
    return blod == "2"

def välj_vapen():
    print("\nVälj ditt vapen:\n1. Svärd\n2. Yxa\n3. Spjut")
    val = int(input("Skriv in ditt val (1, 2, 3): "))
    if val == 1:
        return "svärd", 0.40, 16
    elif val == 2:
        return "yxa", 0.30, 20
    elif val == 3:
        return "spjut", 0.35, 18
    else:
        print("Ogiltigt val, du får svärd som standardvapen.")
        return "svärd", 0.40, 16

def introduktion(vapen):
    print("\nMortis Ludi\n"
          "===========\n"
          "Du är gladiatorn Lady Eater, nu ska du slåss mot gladiatorn Guts.\n"
          "Ni befinner er i en stor romersk arena i Nicaragua omgivna av en förväntansfull publik.\n"
          f"Du är klädd enbart i ett par baggy jeans, Vlone shirt, ett par Jordan 1s, och du råkar vara\n"
          f"6,4 meter lång med dreads och ditt vapen: {vapen}. "
          "Motståndaren har slim jeans och en polo tröja... han vill ha dina kläder.\n"
          "Han ser redo ut att anfalla dig, gör dig redo.\n\nTryck ner enter för att fortsätta...")
    input("")

def starta_strid(healthpoints, fiende, skicklighet, skada, blod):
    lista = ["spark", "slag", "kast"]
    strid = True
    start_tid = time.time()
    tidsgrans = 50
    modighet_spelare = 0
    modighet_fiende = 0

    print("Guts börjar springa emot dig med en arg blick\n")

    while strid:
        fiendeval = random.choice(lista)
        elapsed_time = time.time() - start_tid
        if elapsed_time >= tidsgrans:
            print("Tiden har gått ut! Striden avbryts.")
            break

        print(f"Du har {healthpoints} hälsopoäng kvar.")
        print(f"Guts har {fiende} hälsopoäng kvar.")

        val1 = input("Vilket väljer du, slag, spark, kast eller vapen? ").lower()
        if val1 == "kast":
            modighet_fiende += 2
        else:
            modighet_spelare += 1

        if val1 == "vapen":
            healthpoints, fiende, modighet_fiende = använd_vapen(
                vapen, skicklighet, skada, fiendeval, healthpoints, fiende, blod, modighet_fiende
            )
        else:
            healthpoints, fiende = använd_annan_teknik(val1, fiendeval, healthpoints, fiende, blod)

        if fiende <= 0 or healthpoints <= 0:
            strid = False

    avsluta_strid(elapsed_time, tidsgrans, modighet_spelare, modighet_fiende, healthpoints, fiende)

def använd_vapen(vapen, skicklighet, skada, fiendeval, healthpoints, fiende, blod, modighet_fiende):
    print(f"Guts väljer {fiendeval}")
    if random.random() <= skicklighet:
        print(f"Du använder vapnet: {vapen} och träffar Guts!")
        fiende -= skada
        modighet_fiende += 1
        if blod:
            print(f"Blod flyger när du träffar Guts med vapnet: {vapen}!")
    else:
        print(f"Du missar med vapnet: {vapen}.")
        if fiendeval in ["slag", "kast", "spark"]:
            print(f"Guts använder {fiendeval} och slår bort ditt vapen och skadar dig samtidigt.")
            healthpoints -= 20
    return healthpoints, fiende, modighet_fiende

def använd_annan_teknik(val1, fiendeval, healthpoints, fiende, blod):
    print(f"Guts väljer {fiendeval}")
    if val1 == fiendeval:
        print("Ni båda missar och stirrar argt på varandra.")
    elif val1 == "slag" and fiendeval == "kast":
        healthpoints -= 13
        print("Guts kastar dig i golvet." if not blod else "Guts kastar dig ner i sanden och spräcker flera blodkärl.")
    elif val1 == "slag" and fiendeval == "spark":
        fiende -= 13
        print("Du slår Guts." if not blod else "Du slår en hård uppercut mot Guts och blod och tänder flyger.")
    elif val1 == "spark" and fiendeval == "kast":
        fiende -= 15
        print("Du sparkar ner Guts." if not blod else "Du sparkar Guts i ansiktet och hans skalle spricker.")
    elif val1 == "spark" and fiendeval == "slag":
        healthpoints -= 13
        print("Guts slår dig." if not blod else "Guts slår dig i ansiktet och tänder flyger.")
    elif val1 == "kast" and fiendeval == "spark":
        healthpoints -= 15
        print("Guts sparkar dig." if not blod else "Guts sparkar dig hårt i magen, blod flyger.")
    elif val1 == "kast" and fiendeval == "slag":
        fiende -= 6
        print("Du kastar ner Guts." if not blod else "Du kastar ner Guts i marken och blod sprutar.")
    return healthpoints, fiende

def avsluta_strid(elapsed_time, tidsgrans, modighet_spelare, modighet_fiende, healthpoints, fiende):
    if elapsed_time >= tidsgrans:
        if modighet_spelare > modighet_fiende:
            print("Tiden är slut och du anses vara modigast. Du vinner!")
        elif modighet_fiende > modighet_spelare:
            print("Tiden är slut och Guts anses vara modigast. Han vinner!")
        else:
            print("Striden är oavgjord, ingen var modigast.")
    elif fiende <= 0:
        print("Du vann striden, Yippie!")
    else:
        print("Fienden vann striden.")


healthpoints, fiende = välj_svårighetsgrad()
blod = välj_blodnivå()
vapen, skicklighet, skada = välj_vapen()
clear_terminal()
introduktion(vapen)
clear_terminal()
starta_strid(healthpoints, fiende, skicklighet, skada, blod)


