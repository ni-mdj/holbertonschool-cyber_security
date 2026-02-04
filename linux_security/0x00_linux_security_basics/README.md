# Linux Security Basics

## Description
Short Bash scripts that demonstrate common Linux security checks: login history, active connections, firewall rules, service exposure, auditing, packet capture, and network scanning.

## Resources
- What is the Shell
- What is Kali Linux
- File System Hierarchy
- Linux file system
- Linux Security Command
- What are the Advantages of Using Linux (Cybersecurity)
- Linux Networking
- How to Securely Transfer Files in Linux Using SCP
- How to Set Up a Firewall with UFW on Ubuntu
- Guide to the Linux Firewall

## Learning Objectives
By the end of this project, you should be able to explain:
- What is Linux and what is a Linux command.
- The structure of the Linux operating system.
- The purpose and benefits of the FHS.
- Key directories in the Linux file system and their purposes.
- How to protect files and directories.
- How to monitor and investigate system activity.
- How to securely transfer files and data.
- How to configure and manage a firewall.
- How to identify and terminate malicious processes.
- How to use `ps` and `kill` to identify/stop malicious processes.
- How to use `netstat` and `ss` to monitor network traffic.
- How to use `nmap`, `lynis`, and `tcpdump` to analyze traffic.
- How to use `iptables` and `ufw` to manage firewall rules.

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`.
- Scripts tested on Kali Linux.
- All scripts are exactly two lines long (`wc -l file` prints `2`).
- Substitute the IP range for `$1` when required.
- Files must end with a new line.
- First line of all scripts: `#!/bin/bash`.
- A `README.md` at the root of the project directory is mandatory.
- No backticks, `&&`, `||`, or `;`.
- Code must follow Betty style (`betty-style.pl`, `betty-doc.pl`).
- All files must be executable.

## Project Files
- `0-login.sh`: show the 5 most recent logins using `last`.
- `1-active-connections.sh`: list active TCP connections with `ss`.
- `2-incoming_connections.sh`: allow inbound TCP port 80 using UFW.
- `3-firewall_rules.sh`: list iptables rules with verbose counters.
- `4-network_services.sh`: list listening services with `netstat`.
- `5-audit_system.sh`: run a system audit with Lynis.
- `6-capture_analyze.sh`: capture 5 packets with `tcpdump`.
- `7-scan.sh`: discover live hosts with `nmap -sn` against `$1`.

## Usage
Make scripts executable with `chmod +x <file>` then run:
- `./0-login.sh`
- `./1-active-connections.sh`
- `./2-incoming_connections.sh`
- `./3-firewall_rules.sh`
- `./4-network_services.sh`
- `./5-audit_system.sh`
- `./6-capture_analyze.sh`
- `./7-scan.sh 192.168.1.0/24`

## Repo
- GitHub repository: holbertonschool-cyber_security
- Directory: `linux_security/0x00_linux_security_basics`
- File: `README.md`
