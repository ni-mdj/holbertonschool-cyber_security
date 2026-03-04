# 0x03 - Protocoles & Serveurs (Protocols & Servers)

Ce dossier contient des exercices et ressources sur la gestion des protocoles et serveurs Linux, y compris iptables, pare-feu, et analyse des connexions réseau.

## Objectifs

- Comprendre et configurer les règles **iptables** (pare-feu Linux).
- Analyser et monitorer les connexions réseau et les services actifs.
- Gérer les protocoles de communication et leur sécurité.
- Appliquer les bonnes pratiques en matière de sécurité des serveurs.

## Structure du dossier

### Scripts disponibles

- **0-iptables.sh** : Affiche toutes les règles iptables actuelles avec numéros de ligne en format lisible.
  ```bash
  sudo ./0-iptables.sh
  ```
  Sortie : liste de toutes les chaînes (FILTER, NAT, MANGLE, etc.) avec leur configuration.

## Concepts clés

### iptables - Pare-feu Linux

**iptables** est le principal outil de configuration du pare-feu sur Linux. Il gère les paquets réseau via des **chaînes** et des **tables** :

#### Tables principales
- **filter** : accepter/rejeter/ignorer les paquets (par défaut)
- **nat** : translation d'adresses réseau (port forwarding, masquerading)
- **mangle** : modifier les propriétés des paquets
- **raw** : tracking des connexions
- **security** : SELinux

#### Chaînes (Chains)
- **INPUT** : paquets entrants destinés à la machine
- **OUTPUT** : paquets sortants générés localement
- **FORWARD** : paquets traversant la machine (routage)
- **PREROUTING** / **POSTROUTING** : pour NAT

#### Actions courantes
- **ACCEPT** : accepter le paquet
- **DROP** : rejeter silencieusement
- **REJECT** : rejeter avec notification
- **RETURN** : retourner à la chaîne appelante

### Commandes iptables utiles

```bash
# Afficher les règles actuelles
sudo iptables -L -n -v --line-numbers

# Ajouter une règle (exemple : accepter SSH)
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Supprimer une règle (par numéro de ligne)
sudo iptables -D INPUT 1

# Supprimer toutes les règles
sudo iptables -F

# Sauvegarder les règles (Debian/Ubuntu)
sudo iptables-save > /etc/iptables/rules.v4

# Restaurer les règles
sudo iptables-restore < /etc/iptables/rules.v4
```

### Protocoles courants et ports

| Protocole | Port | Usage |
|-----------|------|-------|
| SSH | 22/tcp | Accès à distance sécurisé |
| HTTP | 80/tcp | Web (non sécurisé) |
| HTTPS | 443/tcp | Web (sécurisé) |
| DNS | 53/udp, 53/tcp | Résolution de noms |
| SMTP | 25/tcp | Email (sortant) |
| POP3 | 110/tcp | Email (entrant) |
| IMAP | 143/tcp | Email (entrant) |
| FTP | 20-21/tcp | Transfert fichiers |
| DHCP | 67-68/udp | Configuration dynamique |

## Exercices courants

1. **Afficher les règles iptables** — voir quelles connexions sont autorisées
2. **Bloquer une adresse IP** — `iptables -A INPUT -s <IP> -j DROP`
3. **Ouvrir un port** — `iptables -A INPUT -p tcp --dport <PORT> -j ACCEPT`
4. **Mettre en place un pare-feu de base** — règles par défaut restrictives
5. **Analyser les connexions actives** — avec `netstat`, `ss` ou `lsof`

## Outils complémentaires

- **netstat** : affiche les statistiques réseau et connexions
- **ss** : socket statistics (remplaçant moderne de netstat)
- **lsof** : liste les fichiers ouverts (incluant les sockets)
- **tcpdump** : capture et analyse les paquets
- **nmap** : scan des ports et services
- **ufw** : interface simplifiée pour iptables (Debian/Ubuntu)

## Bonnes pratiques

- ✓ Toujours sauvegarder les règles iptables avant de les modifier
- ✓ Tester chaque changement avant de le rendre permanent
- ✓ Utiliser des règles restrictives par défaut (whitelisting plutôt que blacklisting)
- ✓ Documenter chaque règle avec un commentaire explicite
- ✓ Monitorer les logs du pare-feu (`/var/log/syslog`, `journalctl`)
- ✗ Ne pas utiliser de ports par défaut pour les services sensibles
- ✗ Ne pas désactiver tous les filtres en cas de problème (diagnostic d'abord)

## Exemple de configuration de base

```bash
#!/bin/bash
# Initialiser avec politique par défaut restrictive
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Accepter les connexions locales
iptables -A INPUT -i lo -j ACCEPT

# Accepter les établissements de connexion existants
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Accepter SSH
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Accepter HTTP/HTTPS
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Accepter ping
iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT

# Sauvegarder
iptables-save > /etc/iptables/rules.v4
```

## Ressources supplémentaires

- [Man page iptables](https://linux.die.net/man/8/iptables)
- [Linux Kernel Networking](https://www.kernel.org/doc/html/latest/networking/index.html)
- [OWASP : Network Segmentation](https://cheatsheetseries.owasp.org/cheatsheets/Network_Segmentation_Cheat_Sheet.html)

