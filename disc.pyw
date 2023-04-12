KEY = "RRAT"
TITLE = "GAME1"

import os

def save():
    f = input("file path (leave empty if default): ")
    if f == "":
        savefile = open("c:/OS/saves/GAME1/save.pyw", "w")
    elif f == "sd":
        savefile = open("d:/sd/game/save.pyw", "w")
    elif f == "usb":
        savefile = open("d:/usb/game/save.pyw", "w")
    prog = input("the game progress: ")
    level = input("the level: ")
    money = input("amount of money: ")
    lives = input("amount of lives: ")
    savefile.writelines([f'prog = {prog}\n', f'level = {level}\n', f'money = {money}\n', f'lives = {lives}\n'])
    savefile.close()
def check():
    try:
        f = input("file path (leave empty if default): ")
        if f == "":
            savefile = open("c:/OS/saves/GAME1/save.pyw", "r")
        elif f == "sd":
            savefile = open("d:/sd/game/save.pyw", "r")
        elif f == "usb":
            savefile = open("d:/usb/game/save.pyw", "r")        
        atr = savefile.read(9000000)
        exec(atr + """print(f"progress = {prog}")
print(f"level = {level}")
print(f"lives = {lives}")
print(f"money = {money}")""")
    except:
        print("cant find save file...")

while 1:
    pick = input("select the mode: ")
    if pick == "save": save()
    elif pick == "check": check()
    elif pick == "exit": break