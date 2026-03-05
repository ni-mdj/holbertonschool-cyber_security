# 0x02 - Forensic Methodologies

## Overview
Ce module couvre les méthodologies et techniques essentielles en investigation numérique (Digital Forensics). L'objectif est de comprendre comment collecter, préserver et analyser les preuves numériques de manière légale et professionnelle.

## Learning Objectives
- Comprendre les principes fondamentaux de la forensique numérique
- Apprendre les meilleures pratiques de préservation des preuves
- Maîtriser les outils et techniques d'investigation
- Analyser les artifacts numériques
- Respecter les protocoles légaux et éthiques

## Méthodologies Clés

### 1. **Chain of Custody (Chaîne de Propriété)**
- Documentation minutieuse de toutes les manipulations
- Signature et date de chaque étape
- Traçabilité complète des preuves
- Prévention de la contamination des données

### 2. **Preservation of Evidence (Préservation des Preuves)**
- Isolation du système compromis
- Création d'images disque bit-à-bit (bit-by-bit)
- Vérification d'intégrité avec les hash (MD5, SHA1, SHA256)
- Archivage sécurisé

### 3. **Analysis Phases (Phases d'Analyse)**

#### a) Pre-Analysis
- Inventaire des preuves
- Documentation des systèmes
- Établissement du périmètre

#### b) Analysis
- Extraction des données
- Recherche de artifacts
- Reconnaissance de patterns
- Reconstruction d'événements

#### c) Post-Analysis
- Compilation des résultats
- Préparation du rapport
- Présentation des preuves

## Outils Communs

### Disk Imaging
- `dd` - Création d'images disque
- `ddrescue` - Récupération avec gestion des erreurs
- `Clonezilla` - Clonage complet de disques

### Analysis Tools
- `Volatility` - Analyse de mémoire volatile
- `Autopsy` - Interface pour The Sleuth Kit
- `FTK Imager` - Acquisition et analyse
- `EnCase` - Plateforme commerciale d'investigation

### Hash & Verification
- `md5sum`, `sha1sum`, `sha256sum`
- Vérification d'intégrité des images

## Best Practices

✓ **À Faire**
- Documenter chaque étape
- Utiliser des outils validés et certifiés
- Travailler sur des copies, jamais sur les originaux
- Vérifier les hash de tous les fichiers
- Respecter les protocoles légaux
- Maintenir la chain of custody
- Utiliser des environnements isolés

✗ **À Éviter**
- Modifier les données originales
- Ignorer la documentation
- Utiliser des outils non validés
- Travailler sans protection (électrostatique, etc.)
- Négliger les aspects légaux

## Types d'Investigations

### Computer Forensics
- Analyse de disques durs
- Investigation sur les systèmes de fichiers
- Récupération de fichiers supprimés

### Mobile Forensics
- Extraction de données de smartphones
- Analyse d'applications
- Récupération de données supprimées

### Network Forensics
- Analyse de logs réseau
- Capture de trafic (PCAP)
- Reconstruction de sessions

### Memory Forensics
- Analyse de RAM
- Extraction de processus actifs
- Récupération d'objets en mémoire

## Challenges de ce Module

### Challenge 0: mystery.txt
**Objectif**: Analyser le fichier `0-mystery.txt` pour extraire des informations forensiques.

**Flag**: `Sherlock_Holbies`

## Ressources Supplémentaires

- [Digital Forensics Documentation](https://en.wikipedia.org/wiki/Digital_forensics)
- [NIST Guidelines](https://csrc.nist.gov/)
- [The Sleuth Kit](https://www.sleuthkit.org/)
- [Volatility Framework](https://www.volatilityfoundation.org/)

## Important Notes

⚠️ **Aspects Légaux et Éthiques**
- Les investigations forensiques doivent respecter la loi
- Nécessite un mandat ou une autorisation
- Les preuves doivent être admissibles en justice
- La confidentialité des données doit être respectée
- Le consentement est généralement requis

## Summary

La forensique numérique est une discipline critique pour :
- Enquêtes criminelles
- Incidents de sécurité
- Litige civil
- Conformité réglementaire
- Récupération de données

Maîtriser ces méthodologies est essentiel pour tout professionnel en cybersécurité.