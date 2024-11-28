import psutil
import os
import platform
import subprocess
import time


# Fonction pour libérer de la mémoire (sur Windows uniquement)
def clean_memory():
    print("Libération de la mémoire...")
    if platform.system() == 'Windows':
        # Sur Windows, il n'y a pas de commande directe pour "libérer" la RAM.
        # Cependant, en tuant certains processus inutiles, nous libérons de la mémoire.
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                # Liste des processus non essentiels à fermer
                non_essential_processes = ['notepad.exe', 'chrome.exe', 'firefox.exe']
                if proc.info['name'] in non_essential_processes:
                    print(f"Arrêt du processus {proc.info['name']} ({proc.info['pid']})")
                    proc.terminate()  # Tuer le processus
                    time.sleep(1)  # Attendre un peu pour s'assurer que le processus est bien arrêté
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass


# Fonction pour optimiser le disque (sur Windows)
def optimize_disk():
    print("Optimisation du disque...")
    if platform.system() == 'Windows':
        # Lancer la défragmentation du disque (Windows)
        try:
            subprocess.run(['defrag', 'C:'], check=True)
            print("Défragmentation terminée.")
        except subprocess.CalledProcessError as e:
            print(f"Erreur de défragmentation : {e}")


# Fonction pour désactiver certains services inutiles
def disable_services():
    print("Désactivation des services non essentiels...")
    # Liste des services à désactiver (exemple pour Windows)
    services_to_disable = ['wuauserv', 'bits', 'uperf', 'OneDrive']

    if platform.system() == 'Windows':
        for service in services_to_disable:
            try:
                subprocess.run(['sc', 'stop', service], check=True)
                subprocess.run(['sc', 'config', service, 'start=', 'disabled'], check=True)
                print(f"Service {service} arrêté et désactivé.")
            except subprocess.CalledProcessError as e:
                print(f"Erreur en désactivant {service}: {e}")


# Fonction pour optimiser l'utilisation des processus et de la mémoire
def optimize_performance():
    print("Optimisation des performances...")
    clean_memory()
    optimize_disk()
    disable_services()

    print("Optimisation terminée.")


# Fonction principale
if __name__ == '__main__':
    optimize_performance()
