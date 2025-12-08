## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- What is Cybersecurity?
- What are the core principles of cybersecurity? (CIA Triad)
- How does encryption contribute to security?
- What is risk management in cybersecurity?
- What are the different types of cybersecurity threats?
- What is the difference between a virus and a worm?
- What is social engineering in the context of security?
- What are the key components of an information security program?
- How do security policies and frameworks contribute to an organization’s security posture?
- What is the purpose of the OWASP Top Ten?
- What is the role of access control in cybersecurity?
- How does multi-factor authentication enhance security?
- What are the common methods for securing a network?

## Requirements
General

- All your files will be run on Kali Linux 2023.2
- Allowed editors: vi, vim, emacs
- You must substitute the IP range for $1.
- The first line of all your files should be exactly #!/bin/bash.
- All your files should end with a new line.
- All your scripts should be less than 2 lines long ($ wc -l file should print <= 2).
- You are not allowed to use backticks, &&, || or ;.
- Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
- You are not Allowed to use Neither Printf.

## Project Overview
Introductory Bash scripts that practice core security tasks:
- `0-release.sh`: print the Linux distribution name.
- `1-gen_password.sh`: generate a random alphanumeric password of given length using `/dev/urandom`.
- `2-sha256_validator.sh`: verify a file’s SHA-256 hash and report OK/FAILED.
- `3-gen_key.sh`: create a 4096-bit RSA SSH key pair via OpenSSH.
- `4-root_process.sh`: list processes for a given user, excluding entries with zero VSZ/RSS.

## Usage
Make scripts executable with `chmod +x <file>` then run:
- `./0-release.sh`
- `./1-gen_password.sh 20`
- `./2-sha256_validator.sh file hash`
- `./3-gen_key.sh new_key`
- `./4-root_process.sh root`
