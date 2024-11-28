import psutil
import platform
import cpuinfo
import socket
import os
from datetime import datetime

# Fonction pour écrire les informations dans un fichier log
def write_log(log_data):
    with open("system_info.log", "a", encoding="utf-8") as log_file:
        log_file.write(log_data)

# Informations générales
log_data = f"### Informations système ({datetime.now()}) ###\n"
log_data += f"Système d'exploitation : {platform.system()} {platform.release()} ({platform.version()})\n"
log_data += f"Architecture : {platform.architecture()[0]}\n"
log_data += f"Nom de l'ordinateur : {platform.node()}\n"
log_data += "\n"  # Espacement

# Affichage dans le terminal
print("### Informations système ###")
print(f"Système d'exploitation : {platform.system()} {platform.release()} ({platform.version()})")
print(f"Architecture : {platform.architecture()[0]}")
print(f"Nom de l'ordinateur : {platform.node()}\n")

# Informations sur le processeur
cpu_info = cpuinfo.get_cpu_info()
cpu_name = cpu_info.get('cpu', 'Nom du processeur non disponible')
cpu_freq = psutil.cpu_freq().current
logical_cores = psutil.cpu_count(logical=True)
physical_cores = psutil.cpu_count(logical=False)

log_data += f"Processeur : {cpu_name}\n"
log_data += f"Fréquence du processeur : {cpu_freq} MHz\n"
log_data += f"Nombre de cœurs logiques : {logical_cores}\n"
log_data += f"Nombre de cœurs physiques : {physical_cores}\n"
log_data += "\n"  # Espacement

# Affichage dans le terminal
print(f"Processeur : {cpu_name}")
print(f"Fréquence du processeur : {cpu_freq} MHz")
print(f"Nombre de cœurs logiques : {logical_cores}")
print(f"Nombre de cœurs physiques : {physical_cores}\n")

# Mémoire
virtual_memory = psutil.virtual_memory()
total_ram = virtual_memory.total / (1024**3)
ram_usage = virtual_memory.percent
free_ram = virtual_memory.available / (1024**3)

log_data += f"Total mémoire RAM : {total_ram:.2f} GB\n"
log_data += f"Utilisation RAM : {ram_usage}%\n"
log_data += f"Memoire libre RAM : {free_ram:.2f} GB\n"
log_data += "\n"  # Espacement

# Affichage dans le terminal
print("### Mémoire ###")
print(f"Total mémoire RAM : {total_ram:.2f} GB")
print(f"Utilisation RAM : {ram_usage}%")
print(f"Memoire libre RAM : {free_ram:.2f} GB\n")

# Mémoire swap
swap_memory = psutil.swap_memory()
total_swap = swap_memory.total / (1024**3)
swap_usage = swap_memory.percent

log_data += f"Total Swap : {total_swap:.2f} GB\n"
log_data += f"Utilisation Swap : {swap_usage}%\n"
log_data += "\n"  # Espacement

# Affichage dans le terminal
print("### Mémoire Swap ###")
print(f"Total Swap : {total_swap:.2f} GB")
print(f"Utilisation Swap : {swap_usage}%\n")

# Disque dur
log_data += "### Disques durs ###\n"
print("### Disques durs ###")

partitions = psutil.disk_partitions()
for partition in partitions:
    try:
        usage = psutil.disk_usage(partition.mountpoint)
        total_disk = usage.total / (1024**3)
        used_disk = usage.used / (1024**3)
        free_disk = usage.free / (1024**3)
        percent_disk = usage.percent

        log_data += f"\nPartition : {partition.device}\n"
        log_data += f"  Total : {total_disk:.2f} GB\n"
        log_data += f"  Utilisé : {used_disk:.2f} GB\n"
        log_data += f"  Libre : {free_disk:.2f} GB\n"
        log_data += f"  Utilisation : {percent_disk}%\n"
        log_data += "\n"  # Espacement

        print(f"\nPartition : {partition.device}")
        print(f"  Total : {total_disk:.2f} GB")
        print(f"  Utilisé : {used_disk:.2f} GB")
        print(f"  Libre : {free_disk:.2f} GB")
        print(f"  Utilisation : {percent_disk}%\n")
    except PermissionError as e:
        print(f"\nPartition {partition.device} : Erreur d'accès, périphérique non prêt.")
        log_data += f"\nPartition {partition.device} : Erreur d'accès, périphérique non prêt.\n"
    except Exception as e:
        print(f"\nPartition {partition.device} : Erreur inconnue - {e}")
        log_data += f"\nPartition {partition.device} : Erreur inconnue - {e}\n"

# Réseau
log_data += f"\n### Réseau ###\n"
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

log_data += f"Nom de l'hôte : {hostname}\n"
log_data += f"Adresse IP : {ip_address}\n"
log_data += "\n"  # Espacement

# Affichage dans le terminal
print("### Réseau ###")
print(f"Nom de l'hôte : {hostname}")
print(f"Adresse IP : {ip_address}\n")

# Carte graphique (Linux uniquement)
if platform.system() == 'Linux':
    log_data += "\n### Carte graphique ###\n"
    print("\n### Carte graphique ###")
    try:
        import subprocess
        graphics_info = subprocess.check_output("lspci | grep VGA", shell=True).decode("utf-8")
        log_data += f"Carte graphique : {graphics_info}\n"
        print(f"Carte graphique : {graphics_info}")
    except Exception as e:
        print(f"Erreur lors de la récupération des informations graphiques : {e}")
        log_data += f"Erreur lors de la récupération des informations graphiques : {e}\n"

# Température du processeur (Linux uniquement)
if platform.system() == 'Linux':
    log_data += "\n### Température du processeur ###\n"
    print("\n### Température du processeur ###")
    try:
        temp = psutil.sensors_temperatures()
        if "coretemp" in temp:
            for sensor in temp["coretemp"]:
                log_data += f"{sensor.label}: {sensor.current}°C\n"
                print(f"{sensor.label}: {sensor.current}°C")
    except Exception as e:
        print(f"Erreur lors de la récupération de la température : {e}")
        log_data += f"Erreur lors de la récupération de la température : {e}\n"

log_data += "\n### Fin des informations système ###\n\n"
write_log(log_data)
print("\n### Fin des informations système ###")


