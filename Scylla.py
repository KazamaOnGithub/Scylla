# liste des modules utiliser
import time
from pystyle import *

############################
# Author: KazamaOnGithub   #
# Discord: .gg/backfire    #
# Github : @KazamaOnGithub #
############################

############################################################################################################
# Je ne trouve pas de bon module pour les couleurs c'est pour ceci que c'est horrible niveau interface x'( #
############################################################################################################


# def du tool
def tool():
    banner = print(Colorate.Horizontal(Colors.yellow_to_red, """

                                                           _._
                                                       __.{,_.).__
                                                    .-"           "-.
                                                  .'  __.........__  '.
                                                 /.-'`___.......___`'-.\ 
                                                /_.-'` /   \ /   \ `'-._\ 
                                                |     |   '/ \ '  |     |
                                                |      '-'     '-'      |
                                                ;                       ;
                                                _\         ___         /_
                                               /  '.'-.__  ___  __.-'.'  \ 
                                             _/_    `'-..._____...-'`    _\_
                                            /   \           .           /   \ 
                                            \____)          .          (____/
                                                \___________.___________/
                                                  \___________________/
                                                 (_____________________)
                                    
                                    "Backup logins in express, join discord.gg/backfire"

------------------------------------------------------------------------------------------------------------------------"""))
    print()
    filename = input(Colorate.Vertical(Colors.yellow_to_red, " [>] Enter the file name? "))
    fichier = open(filename + ".txt", "x")
    print()
    print(Colorate.Vertical(Colors.yellow_to_red, " [i] The name of the file to be created was!"))
    print()
    # variable info necessaire
    site_logiciel = input(Colorate.Vertical(Colors.yellow_to_red, " [>] name of website or software? "))
    print()
    mail_phone_username = input(Colorate.Vertical(Colors.yellow_to_red, " [>] e-mail or phone number or username? "))
    print()
    password = input(Colorate.Vertical(Colors.yellow_to_red, " [>] password? "))
    print()
    description = input(Colorate.Vertical(Colors.yellow_to_red, " [>] description (ex: roblox account with 2k robux)? "))
    # écriture dans le fichier
    fichierbis = open(filename + ".txt", "a")
    fichierbis.write(site_logiciel + " :: " + mail_phone_username + " :: " + password + " :: " + description)
    fichier.close()
    print()
    print(Colorate.Vertical(Colors.yellow_to_red, "Your information has been recorded and written!"))
    

tool()

############################
# Author: KazamaOnGithub   #
# Discord: .gg/backfire    #
# Github : @KazamaOnGithub #
############################
    