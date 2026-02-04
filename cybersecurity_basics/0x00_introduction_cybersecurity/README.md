# Introduction to Cybersecurity

## Description
Introductory Bash scripts that practice core security tasks: system identification, password generation, hashing verification, SSH key creation, and process inspection.

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- What is cybersecurity?
- What are the core principles of cybersecurity (CIA triad)?
- How does encryption contribute to security?
- What is risk management in cybersecurity?
- What are the different types of cybersecurity threats?
- What is the difference between a virus and a worm?
- What is social engineering in the context of security?
- What are the key components of an information security program?
- How do security policies and frameworks contribute to an organization's security posture?
- What is the purpose of the OWASP Top Ten?
- What is the role of access control in cybersecurity?
- How does multi-factor authentication enhance security?
- What are the common methods for securing a network?

## Requirements
- All files will be run on Kali Linux 2023.2.
- Allowed editors: `vi`, `vim`, `emacs`.
- Substitute the IP range for `$1` when required.
- The first line of all scripts should be exactly `#!/bin/bash`.
- All files should end with a new line.
- All scripts should be less than 2 lines long (`wc -l file` should print <= 2).
- You are not allowed to use backticks, `&&`, `||`, or `;`.
- Your code should use the Betty style (checked with `betty-style.pl` and `betty-doc.pl`).
- You are not allowed to use `printf`.

## Project Files
- `0-release.sh`: print the Linux distribution name.
- `1-gen_password.sh`: generate a random alphanumeric password of a given length using `/dev/urandom`.
- `2-sha256_validator.sh`: verify a file's SHA-256 hash and report OK/FAILED.
- `3-gen_key.sh`: create a 4096-bit RSA SSH key pair via OpenSSH.
- `4-root_process.sh`: list processes for a given user, excluding entries with zero VSZ/RSS.

## Usage
Make scripts executable with `chmod +x <file>` then run:
- `./0-release.sh`
- `./1-gen_password.sh 20`
- `./2-sha256_validator.sh file hash`
- `./3-gen_key.sh new_key`
- `./4-root_process.sh root`

## Repo
- GitHub repository: holbertonschool-cyber_security
- Directory: `cybersecurity_basics/0x00_introduction_cybersecurity`
- File: `README.md`
