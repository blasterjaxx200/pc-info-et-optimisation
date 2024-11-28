import os
import fade
import time
from fade import *

banner = r"""
 /$$            /$$$$$$                                   
|__/           /$$__  $$                                  
 /$$ /$$$$$$$ | $$  \__//$$$$$$         /$$$$$$   /$$$$$$$
| $$| $$__  $$| $$$$   /$$__  $$       /$$__  $$ /$$_____/
| $$| $$  \ $$| $$_/  | $$  \ $$      | $$  \ $$| $$      
| $$| $$  | $$| $$    | $$  | $$      | $$  | $$| $$      
| $$| $$  | $$| $$    |  $$$$$$/      | $$$$$$$/|  $$$$$$$
|__/|__/  |__/|__/     \______/       | $$____/  \_______/
                                      | $$                
                                      | $$                
                                      |__/           
"""
banner = fade.fire(banner)

menu = """
                   ╔════════════════════════╗
                   ║                        ║                          
                   ║ [1]  pc info           ║               
                   ║                        ║                           
                   ║ [2] optimisation pc    ║
                   ║                        ║                           
                   ╚════════════════════════╝
"""
menu = fade.fire(menu)

def clear_screen():
    """Clear the console screen depending on the OS."""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux
        os.system('clear')

def main():
    clear_screen()  # Nettoie l'écran
    print(banner)  # Affiche le banner en dégradé de feu
    print(menu)  # Affiche le menu

    choice = input("choice : ")

    if choice == "1":
        os.system("python src/tool1.py")
    elif choice == "2":
        os.system("python src/tool2.py")
    elif choice == "3":
        os.system("python src/tool3.py")

        # Utilisation du chemin complet ou relatif compatible Windows
        os.system(r'src\\Builder.bat')  # ou utilise le chemin complet
    else:
        print("Merci de rentrer un nombre valide.")
        time.sleep(1)  # Pause pour afficher l'erreur
        main()  # Réaffiche le menu

main()