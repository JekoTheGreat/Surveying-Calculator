# [ PROPERTY OF JekoTheGreat, Copyright 2026, All rights reserved. ] #
# [ My first Python program, python is terrible. Learn anything else, like no joke. ] #

import math
import os

mode = input("Enter your desired mode [Average DMS, DMS to Degrees]: ")

def lower(string):
    newString = string.lower()
    return newString

def getFreshDMS():
    return {"degrees": 0, "minutes": 0, "seconds": 0}

if mode.lower() == lower("Average DMS"): # Alternatively, these can just be lowercase... Functions are more fun lol
    
    os.system('cls')

    ui1 = int(input("How many angles: "))
    sum = getFreshDMS()

    for i in range(ui1):
        print("\nAngle", i + 1, "\n")
        degrees = int(input("Please input the number of degrees: "))
        sum["degrees"] += degrees
        minutes = int(input("Please input the number of minutes: "))
        sum["minutes"] += minutes
        seconds = int(input("Please input the number of seconds: "))
        sum["seconds"] += seconds

    avg = {"degrees": sum["degrees"] / ui1, "minutes": sum["minutes"] / ui1, "seconds": sum["seconds"] / ui1}
    print("Your angles averaged: ", avg,"\n")
    print("You may need to adjust some values sicne they may be improper.")
    input("Press enter to continue...")

    #print("Did average.")

elif mode.lower() == lower("DMS to Degrees"):

    os.system('cls')

    DFloat = 0 # DFloat is Degrees Float, this will be the output after the conversion.
    DFloat += int(input("Input the number of degrees: "))
    DFloat += int(input("Input the number of minutes: ")) / 60
    DFloat += int(input("Input the number of seconds: ")) / 3600

    print("\nYour angle converted: ", DFloat, "\n")
    input("Press enter to continue...")

