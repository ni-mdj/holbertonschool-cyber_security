# Passive Reconnaissance

Collect public information about a target without direct interaction beyond public DNS/WHOIS sources. Scripts are short Bash commands that automate common passive recon queries.

## Learning Objectives
- Use WHOIS and DNS records to gather ownership and infrastructure clues.
- Identify A, MX, and TXT records for a domain.
- Aggregate DNS answers for quick review.
- Enumerate subdomains using passive sources.

## Tools
- `whois`, `nslookup`, `dig`
- `subfinder` (ProjectDiscovery)

## Project Files
- `0-whois.sh`: run WHOIS and extract registrant/admin/tech lines to `<domain>.csv`.
- `1-a_record.sh`: query A records with `nslookup`.
- `2-mx_record.sh`: query MX records with `nslookup`.
- `3-txt_record.sh`: query TXT records with `nslookup`.
- `4-dig_all.sh`: fetch all DNS answers with `dig`.
- `5-subfinder.sh`: enumerate subdomains and write to `<domain>.txt`.
- `holbertonschool_report.md`: short passive recon report (sample target).
- `100-flag.txt`, `101-flag.txt`, `102-flag.txt`: task validation flags.

## Usage
Make scripts executable with `chmod +x <file>` then run:
- `./0-whois.sh example.com`
- `./1-a_record.sh example.com`
- `./2-mx_record.sh example.com`
- `./3-txt_record.sh example.com`
- `./4-dig_all.sh example.com`
- `./5-subfinder.sh example.com`

## Notes
- Run reconnaissance only on domains you are authorized to test.
