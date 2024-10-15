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

clear_terminal()
#intro
blod = int(input("Välj mängden blodbeskrivningar: skriv '1' för mindre blod och '2' för mer blod "))

if blod == 1:
    blod = True
else:
    blod = False


print("Mortis Ludi\n""===========\n""Du är gladiatorn Lady Eater, nu ska du slåss mot gladiatorn Guts.\n""Ni befinner er i en stor romersk arena i Nicaragua omgivna av en förväntansful \npublik."" Ni har inga vapen eller rustning utan du är klädd enbart i ett par\n""baggy jeans, Vlone shirt, ett par jordan 1s och du mot all förmodan \nråkar vara 6,4 meter lång med dreads."" Motståndaren har slim jeans \noch en polo tröja... han vill ha dina kläder.\n""Han ser redo ut att anfalla dig, gör dig redo.\n\nTryck ner enter för att fortsätta...")
input("")

time.sleep(1)
clear_terminal()

healthpoints = 10
fiende = 1
lista = ["spark", "slag", "kast"]
strid = True

print("Guts börjar springa emot dig med en arg blick\n")

while strid == True:
    fiendeval = random.choice(lista)

    print(f"Du har {healthpoints} hälsopoäng kvar.")
    print(f"Guts har {fiende} hälsopoäng kvar.")

    val1 = input("Vilket väljer du, slag, spark eller kast? ").lower()
    print("Guts väljer", fiendeval)


    if val1 == fiendeval:
        print("You both miss and look at each other with disgust.")
    
   
    elif val1 == "slag" and fiendeval == "kast":
        if blod == True:
            print("Guts kastar dig ner i sanden och spräcker flera blodkärl i din kropp. Det flyter ut blod ur din mun. ")
        elif blod == False:
            print("Guts kastar dig i golvet.")
        healthpoints -= 3
        print(f"Du har {healthpoints} hälsopoäng kvar.")
    
  
    elif val1 == "slag" and fiendeval == "spark":
        if blod == True:
            print("Du slår en hård uppercut mot Guts innan han hinner sparka dig. Blod och tänder kastas ut ur hans mun")
        elif blod == False:
            print("Du slår fienden innan den hinner sparka dig.")
        fiende -= 3
        print(f"Fienden har {fiende} hälsopoäng kvar.")
    

    elif val1 == "spark" and fiendeval == "kast":
        if blod == True:
            print("Du sparkar Guts i anisktet och bbunononjnon")
        elif blod == False:
            print("Du sparkar ner fienden på marken.")
        fiende -= 5
        print(f"Fienden har {fiende} hälsopoäng kvar.")
    
    elif val1 == "spark" and fiendeval == "slag":
        print("Fienden slår dig innan du hinner sparka.")
        healthpoints -= 3
        print(f"Du har {healthpoints} hälsopoäng kvar.")
    
    elif val1 == "kast" and fiendeval == "spark":
        print("Fienden sparkar dig innan du hinner kasta honom.")
        healthpoints -= 5
        print(f"Du har {healthpoints} hälsopoäng kvar.")
    
    elif val1 == "kast" and fiendeval == "slag":
        print("Du kastar ner fienden i marken innan han slår dig.")
        fiende -= 3
        print(f"Fienden har {fiende} hälsopoäng kvar.")
    
    if fiende <= 0 or healthpoints <= 0:
        strid = False

if fiende <= 0:
    print("Du vann striden. Den här gången...")
else:
    print("Fienden vann striden.")
    