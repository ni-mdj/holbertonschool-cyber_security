# Nmap Live Hosts Discovery

## Description
Practice Nmap host discovery techniques using ARP, ICMP, TCP, and UDP probes. Each script runs a ping scan (`-sn`) with a different probe type to compare results on the same target range.

## Learning Objectives
- Use Nmap host discovery options to detect live hosts.
- Understand differences between ARP, ICMP, TCP SYN/ACK, and UDP probes.
- Run scans against authorized ranges only.

## Requirements
- `nmap` installed.
- Provide the target range as `$1` (example: `192.168.1.0/24`).

## Project Files
- `0-arp_scan.sh`: ARP ping scan (`nmap -sn -PR`).
- `1-icmp_echo_scan.sh`: ICMP echo request scan (`nmap -sn -PE`).
- `2-icmp_timestamp_scan.sh`: ICMP timestamp scan (`nmap -sn -PP`).
- `3-icmp_address_mask_scan.sh`: ICMP address mask scan (`nmap -sn -PM`).
- `4-tcp_syn_ping.sh`: TCP SYN ping scan on ports 22/80/443 (`nmap -sn -PS22,80,443`).
- `5-tcp_ack_ping.sh`: TCP ACK ping scan on ports 22/80/443 (`nmap -sn -PA22,80,443`).
- `6-udp_ping_scan.sh`: UDP ping scan on ports 53/161/162 (`nmap -sn -PU53,161,162`).
- `100-flag.txt`: task validation flag.

## Usage
Make scripts executable with `chmod +x <file>` then run:
- `./0-arp_scan.sh 192.168.1.0/24`
- `./1-icmp_echo_scan.sh 192.168.1.0/24`
- `./2-icmp_timestamp_scan.sh 192.168.1.0/24`
- `./3-icmp_address_mask_scan.sh 192.168.1.0/24`
- `./4-tcp_syn_ping.sh 192.168.1.0/24`
- `./5-tcp_ack_ping.sh 192.168.1.0/24`
- `./6-udp_ping_scan.sh 192.168.1.0/24`

## Notes
- Run scans only on networks you are authorized to test.

## Repo
- GitHub repository: holbertonschool-cyber_security
- Directory: `network_security/0x04_nmap_live_hosts_discovery`
- File: `README.md`
