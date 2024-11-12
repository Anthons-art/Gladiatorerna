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
    else:
        os.system('clear')

clear_terminal()
time.sleep(1)

blod = int(input("Välj mängden blodbeskrivningar: skriv '1' för mindre blod och '2' för mer blod "))
if blod == 2:
    blod = True
    print("Beskrivningarna blir blodigare.")
else:
    blod = False
    print("Beskrivningarna blir mindre blodiga.")

print("\nVälj ditt vapen:\n1. Svärd\n2. Yxa\n3. Spjut")
vapenval = int(input("Skriv in ditt val (1, 2, 3): "))
if vapenval == 1:
    vapen = "svärd"
    skicklighet = 0.40
    skada = 16
elif vapenval == 2:
    vapen = "yxa"
    skicklighet = 0.30
    skada = 20
elif vapenval == 3:
    vapen = "spjut"
    skicklighet = 0.35
    skada = 18
else:
    print("Ogiltigt val, du får svärd som standardvapen.")
    vapen = "svärd"
    skicklighet = 0.40
    skada = 16

print(f"\nVill du specialisera dig på ditt valda vapen {vapen}?")
specialisering = input("Skriv 'ja' för att specialisera dig, annars skriv 'nej': ").lower() == 'ja'
if specialisering:
    skicklighet += 0.10  
    skada += 5  
    modighet_spelare = -2
    print(f"Du har specialiserat dig på {vapen}! Din skicklighet och skada är nu förbättrad.\nMen din modighet gick ner till {modighet_spelare}")
else:
    modighet_spelare = 1
    print(f"Du har inte specialiserat dig på {vapen}! Din modighet går upp med {modighet_spelare}.\n")

time.sleep(5)

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
start_tid = time.time()
tidsgrans = 50
modighet_fiende = 0

print("Guts börjar springa emot dig med en arg blick\n")

while strid:
    fiendeval = random.choice(lista)
    nu_tid = time.time()
    elapsed_time = nu_tid - start_tid
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

    print(f"Guts väljer {fiendeval}")
    if val1 == "vapen":
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
    else:
        if val1 == fiendeval:
            print("Ni båda missar och stirrar argt på varandra.")
        elif val1 == "slag" and fiendeval == "kast":
            print("Guts kastar dig i golvet." if not blod else "Guts kastar dig ner i sanden och spräcker flera blodkärl.")
            healthpoints -= 13
        elif val1 == "slag" and fiendeval == "spark":
            print(f"Du slår Guts." if not blod else "Du slår en hård uppercut mot Guts och blod och tänder flyger.")
            fiende -= 13
        elif val1 == "spark" and fiendeval == "kast":
            print(f"Du sparkar ner Guts." if not blod else "Du sparkar Guts i ansiktet och hans skalle spricker.")
            fiende -= 15
        elif val1 == "spark" and fiendeval == "slag":
            print(f"Guts slår dig." if not blod else "Guts slår dig i ansiktet och tänder flyger.")
            healthpoints -= 13
        elif val1 == "kast" and fiendeval == "spark":
            print(f"Guts sparkar dig." if not blod else "Guts sparkar dig hårt i magen, blod flyger.")
            healthpoints -= 15
        elif val1 == "kast" and fiendeval == "slag":
            print(f"Du kastar ner Guts." if not blod else "Du kastar ner Guts i marken och blod sprutar.")
            fiende -= 13

    if fiende <= 0 or healthpoints <= 0:
        strid = False

kejsarens_beslut = random.choice([True, False])
if kejsarens_beslut:
    print("\nKejsaren är närvarande och kommer att avgöra din öde...")
    if random.choice([True, False]):
        print("Kejsaren höjer tummen upp - du får leva!")
    else:
        print("Kejsaren sänker tummen... du möter ditt öde.")
else:
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

