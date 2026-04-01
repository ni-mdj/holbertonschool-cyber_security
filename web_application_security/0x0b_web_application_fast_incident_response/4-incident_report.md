# Rapport d'incident - Attaque DoS

## Introduction
Ce rapport présente une attaque web détectée dans `logs.txt`.
Une seule IP a envoyé trop de requêtes en peu de temps.
Ce comportement ressemble à une tentative de Denial of Service (DoS).

## Analyse détaillée de l'attaque
- IP source de l'attaque : `<ATTACKER_IP>`
- Point d'entrée le plus ciblé : `<TARGET_ENDPOINT>`
- Nombre de requêtes envoyées par l'attaquant : `<ATTACK_REQUEST_COUNT>`
- Outil/librairie principal (agent utilisateur) : `<ATTACK_TOOL>`

Ce qui a été observé :
- Un trafic très élevé depuis une seule IP.
- Des requêtes répétées vers le même endpoint.
- Un comportement automatisé.

## Stratégie de mitigation proposée
Solution principale : activer une **limitation de débit** au niveau du proxy inverse ou du WAF.

Protections complémentaires :
- Blocage temporaire des IP abusives.
- Règles WAF simples contre les pics de trafic.
- Limites plus strictes sur les délais d'attente et le nombre de connexions.

## Justification de la solution
La limitation de débit est simple, rapide à déployer et efficace contre ce type d'attaque.
Il protège le serveur avant que les requêtes n'atteignent l'application.
C'est une mesure standard en sécurité web.

## Étapes d'implémentation
1. Mesurer le trafic normal (niveau de référence).
2. Définir une limite par IP.
3. Renvoyer `429 Too Many Requests` quand la limite est atteinte.
4. Ajouter un blocage temporaire des récidivistes.
5. Tester, déployer, puis ajuster les seuils.

Exemple (Nginx) :
```nginx
limit_req_zone $binary_remote_addr zone=per_ip:10m rate=10r/s;

server {
    location / {
        limit_req zone=per_ip burst=20 nodelay;
        limit_req_status 429;
        proxy_pass http://app_backend;
    }
}
```

## Surveillance après mise en place
Surveiller :
- Requêtes par IP
- Réponses HTTP 429
- Erreurs 4xx/5xx
- CPU/RAM/connexions
- Anomalies d'agent utilisateur

Mettre des alertes pour réagir rapidement en cas de nouveau pic.

## Conclusion
L'incident correspond à un schéma DoS automatisé.
La meilleure mitigation immédiate est : limitation de débit + blocage temporaire + surveillance.
Cela réduit le risque et aide à maintenir la disponibilité du service.

---

## Valeurs À Compléter Avant Soumission
Exécuter :
```bash
cd web_application_security/0x0b_web_application_fast_incident_response
ATTACKER_IP=$(./0-attack_ip.sh)
TARGET_ENDPOINT=$(./1-endpoint.sh)
ATTACK_REQUEST_COUNT=$(./2-count_attack.sh)
ATTACK_TOOL=$(./3-library.sh)
```

Remplacer :
- `<ATTACKER_IP>`
- `<TARGET_ENDPOINT>`
- `<ATTACK_REQUEST_COUNT>`
- `<ATTACK_TOOL>`
