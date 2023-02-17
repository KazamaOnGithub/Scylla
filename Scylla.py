# liste des modules utiliser
import time, os, colorama, sys
from colorama import Fore,Style,Back, init
from pystyle import *

############################
# Author: KAZAM[A]#9629    #
# Discord: .gg/soon...     #
# Github : @KazamaOnGithub #
############################

############################################################################################################
# Je ne trouve pas de bon module pour les couleurs c'est pour ceci que c'est horrible niveau interface x'( #
############################################################################################################

# parametre
Cursor.HideCursor()

# Liste de qlq variables

choice_info = " [" + Fore.MAGENTA + ">" + Fore.WHITE + "]"
choice_i = " [" + Fore.GREEN + "i" + Fore.WHITE + "]" 

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.00000001)
# def du tool
def tool():
    os.system( "title 𝘿𝙚𝙫 𝙗𝙮 𝙆𝘼𝙕𝘼𝙈𝘼" )
    os.system("cls")
    banner = (Colorate.Vertical(Colors.purple_to_red, """

                 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄            ▄            ▄▄▄▄▄▄▄▄▄▄▄ 
                ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌          ▐░▌          ▐░░░░░░░░░░░▌
                ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░█▀▀▀▀▀▀▀█░▌
                ▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░▌
                ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌
                ▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░▌          ▐░▌          ▐░░░░░░░░░░░▌
                 ▀▀▀▀▀▀▀▀▀█░▌▐░▌           ▀▀▀▀█░█▀▀▀▀ ▐░▌          ▐░▌          ▐░█▀▀▀▀▀▀▀█░▌
                          ▐░▌▐░▌               ▐░▌     ▐░▌          ▐░▌          ▐░▌       ▐░▌
                 ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌
                ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
                 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
                                                                               
"""))
    # exploiter la variable --> banner
    print(banner)

    filename = input(" \n\n "+ choice_info +  " Give your new file a name :: ")
    fichier = open(filename + ".txt", "x")
    print("   " + choice_i + " The name of the file to be created was!")
    # variable info necessaire
    site_logiciel = input("\n " + choice_info + " Name of website or software? ")
    print("   " + choice_i + " The name was registered!")
    mail_phone_username = input(" \n "+ choice_info +  " E-mail or phone number or username? ")
    print("   " + choice_i + " The information is recorded!")
    password = input("\n "+ choice_info +  " password? ")
    print("   " + choice_i + " Passord has saved with successfully")
    description = input(" \n "+ choice_info +  " Description (ex: roblox account with 2k robux)? ")
    # écriture dans le fichier
    fichierbis = open(filename + ".txt", "a")
    fichierbis.write(site_logiciel + " :: " + mail_phone_username + " :: " + password + " :: " + description)
    fichier.close()
    
    os.system("cls")

    print(Center.XCenter(Center.YCenter(Box.DoubleCube("Your text file was created ═══> " + filename))))
    print("\n" * 13)
    os.system("pause")

tool()


############################
# Author: KAZAM[A]#9629    #
# Discord: .gg/soon...     #
# Github : @KazamaOnGithub #
############################
    
