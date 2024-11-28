# PC Optimizer Tool

Cet outil Python permet d'afficher des informations détaillées sur votre PC, telles que les spécifications du processeur, de la mémoire, du disque dur et plus encore. De plus, il offre des fonctionnalités pour optimiser les performances du système, telles que la désactivation des services non essentiels.

## Fonctionnalités

- **Affichage des informations système** :
  - Nom et modèle du processeur
  - Mémoire RAM installée et utilisée
  - Espace disque disponible et utilisé
  - Températures des composants (si disponibles)
  
- **Optimisation des performances** :
  - Désactivation de services non essentiels (ex. : Windows Update, OneDrive)
  - Réduction de l'utilisation du processeur et de la mémoire

- **Export des informations** :
  - Sauvegarde des informations système dans un fichier texte pour consultation ultérieure.

## Prérequis

Avant d'utiliser cet outil, vous devez avoir les éléments suivants installés sur votre machine :

- **Python 3.x** : Téléchargez et installez Python depuis [python.org](https://www.python.org/).
- **Modules Python requis** :
  - `psutil` : Pour récupérer des informations système et gérer les services.
  - `cpuinfo` : Pour obtenir des détails sur le processeur.
  - `platform` : Pour obtenir des informations sur le système d'exploitation.


