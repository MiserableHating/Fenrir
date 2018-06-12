# A propos
Fenrir est un ransomware codé en python par moi.
Pour le moment, il n'y a rien de dangereux.
Il ne crypte pas encore les données du disque dur mais juste un seul fichier par un seul fichier selon le choix de l'utilisateur.
On ne peut pas encore payer. (Et dans la version finale, on aura pas à le faire)

Voici la clé de décryptage actuelle : SmUgc2FpcyB0b3V0
Plus tard, elle changera au hasard en fonction de l'ordinateur sur lequel Fenrir s'installe.

# Installation :

1. Avoir Python 3.
2. Avoir une version de Visual Studio (La dernière, plus précisement.)
3. Windows+r -> cmd
4. cd C:\Program Files (x86)\Microsoft Visual Studio\2017\BuildTools\VC\Auxiliary\Build
vcvarsall amd64
5. cd \
set CL=-FI"%VCINSTALLDIR%\tools\msvc\14.13.26128\include\stdint.h"
6. pip install pycrypto
7. Ouvrir le fichier lib de Crypto. (C:\Users\Le nom de votre PC\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\Crypto\Random\OSRNG)
8. Ouvrir nt.py avec un éditeur de texte.
9. Modifier "import winrandom" en "from . import winrandom" puis enregistrer.
10. Ouvrir compile.bat
11. Ouvrir le fichier Fenrir.exe dans \dist
