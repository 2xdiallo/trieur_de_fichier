#Programme de Trieur de fichier
#Auteur : 2xdiallo
#ce script permet d'automatiser le tri des fichiers telecharges en les mettant
#dans les dossiers correspondants grace a leur extesions . 

import time
from pathlib import Path
from pprint import pprint


time.sleep(5)

#chemin vers le dossier Download
chemin = Path(r"C:\Users\win10\Downloads")
dictionnaire = {      ".mp3": "Musique",
                      ".wav": "Musique",
                      ".mp4": "Videos",
                      ".avi": "Videos",
                      ".gif": "Videos",
                      ".bmp": "Images",
                      ".png": "Images",
                      ".jpg": "Images",
                      ".txt": "Documents",
                      ".pptx": "Documents",
                      ".csv": "Documents",
                      ".xls": "Documents",
                      ".odp": "Documents",
                      ".pages": "Documents",
                      ".torrent":"Torrents",
                      ".pdf":"Documents",
                      ".rar":"Compressed",
                      ".zip":"Compressed",
                      "":"Autres"

                }
#on cree les dosiers contenu dans le dictionnaire               
for dossier in dictionnaire.values():
    dos = chemin.joinpath(dossier)
    dos.mkdir(exist_ok=True)

#on traverse tous les fichiers contenus dans le dossier download et on deplace le fichier dans le dossier qu'il correspond 
for element in chemin.iterdir():
    if element.is_file() and (element.suffix in dictionnaire):
        if (chemin / dictionnaire[element.suffix] / element.name).is_file():
            continue
        element.rename(chemin / dictionnaire[element.suffix] / element.name )
    elif element.is_file() and (element.suffix not in dictionnaire):
            element.rename(chemin / dictionnaire[""] / element.name )

print("+"*60 )
print("Tous les fichiers ont ete bien ordonnes avec succes -_- ... ") 
print("+"*60 )














