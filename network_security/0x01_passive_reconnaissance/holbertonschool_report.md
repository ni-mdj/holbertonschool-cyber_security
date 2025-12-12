# Passive Reconnaissance Report – holbertonschool.com

## Scope
- Target domain: `holbertonschool.com` and observed subdomains.
- Source: Shodan snapshots (timestamps late 2025).

## Observed IPs / Hosts (Shodan)
- `apply.holbertonschool.com`: 13.39.187.93, 15.236.177.62, 13.38.203.16, 13.37.52.4, 35.181.125.81, 35.181.28.191 (AWS eu-west-3).
- `staging-apply.holbertonschool.com`: 35.181.84.105, 15.236.53.167 (AWS eu-west-3).
- `read.holbertonschool.com`: 52.47.114.157 (AWS eu-west-3).
- `yriry2.holbertonschool.com`: 52.47.143.83 (AWS eu-west-3).
- Reverse DNS points to AWS EC2 hosts (eu-west-3).

## Technologies / Frameworks
- Web server: `nginx/1.20.0` on apply/staging/read hosts.
- TLS: TLSv1.2 (some also support TLSv1.3 on yriry2); certificates issued by Amazon RSA 2048 (M02/M04) and Let’s Encrypt (E8 for yriry2).
- Headers: `X-Frame-Options: SAMEORIGIN`, `X-XSS-Protection: 1; mode=block` (yriry2 shows `0`), `X-Content-Type-Options: nosniff`, `X-Download-Options: noopen/noop...`.
- Likely stack: AWS-hosted, nginx front-end; application appears to be Holberton admission portal (“Welcome to Holberton School admission portal”).

## Notes
- Multiple IPs for `apply.holbertonschool.com` suggest load balancing/rotation on AWS.
- Staging and production separated (`staging-apply` vs `apply`), both exposed over HTTPS with nginx.
- Access control varies: some hosts return `401 Unauthorized` (staging, read), others `200 OK` (apply).
