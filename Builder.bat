@echo off
echo Installation du module fade...
pip install fade
pip install time
pip install psutil
pip install platform
pip install py-cpuinfo

pip install socket
if %errorlevel% neq 0 (
    echo Erreur lors de l'installation du module fade. Assurez-vous que pip est correctement installé.
    exit /b
)

echo Lancement de main.py...
python main.py
