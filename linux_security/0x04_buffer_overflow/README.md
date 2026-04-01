# 0x04 - Buffer Overflow

## Task 0: Hack the VM

Ce dossier contient le script `read_write_heap.py`.

Le script permet de:
- lire uniquement la zone `[heap]` d'un processus Linux,
- chercher une chaîne ASCII,
- remplacer cette chaîne par une autre.

## Usage

```bash
sudo python3 read_write_heap.py pid search_string replace_string
```

Exemple:

```bash
sudo python3 read_write_heap.py 6515 Holberton maroua
```
