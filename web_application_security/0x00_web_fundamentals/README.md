# Web Fundamentals

Project badge: 0%

Level: Amateur

Author: Yosri Ghorbel

Weight: 2

Your score will be updated as you progress.

## Description
This project introduces core web fundamentals and basic web application security concepts.

## Resources
Read or watch:
- How the Web works?
- The Fundamentals of Web Development
- Web 1.0 vs Web 2.0 vs Web 3.0
- What are Progressive Web Apps?
- Stateful vs Stateless - Web App Design
- Structured vs. Unstructured Data
- Web Application Security Explained
- Web Application Security Testing

References:
- Stateful vs Stateless
- How Does the Frontend Communicate with the Backend?
- OWASP Top Ten
- Cross-Origin Resource Sharing (CORS)
- Bug bounty program
- Top Bug Bounty Programs

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- How the Web works
- Examples of Web Applications
- Web 1.0 vs Web 2.0 vs Web 3.0
- PWA - Progressive Web Applications
- How does the Front-End communicate with the Back-End?
- Stateful vs Stateless: what's the difference?
- Structured vs Unstructured: what's the difference?
- Web Application Security Risks
- Bug Bounty Programs

## Requirements
General:
- All your scripts will be tested on Kali Linux 2023.3
- All your scripts should be exactly two lines long (`wc -l file` prints 2)
- You must substitute the IP range for `$1`
- All your files should end with a new line
- The first line of all your files should be exactly `#!/bin/bash`
- A README.md file at the root of the project directory is mandatory
- Your code should use the Betty style (checked with `betty-style.pl` and `betty-doc.pl`)
- All your files must be executable

## More Info
Install curl:
```bash
sudo apt install curl
```

Check curl version:
```bash
curl --version
```

Install SQLmap:
```bash
sudo apt install sqlmap
```

Check SQLmap version:
```bash
sqlmap --version
```

## Tasks
### 0. Welcome
Welcome to Web Application Security Module \o/

Brief discussion:
```
Colleague:
Hear this, My Boss Just asked me for Customer Support Dashboard.

Me:
And? For a Dashboard with Supports UI, Customers UI and Admin Portal will take you at least 4 weeks.

Colleague:
I challenged him to do it within 3 days for reward ;)

Me:
Are you serious :O?

Colleague:
Yeah, I got Paid ChatGPT 4 by my side :'D

...

3 Days later.

...

Colleague:
I already finished it, take a look my friend http://web0x00.hbtn!

Me:
Am I allowed to pentest it :p?

Colleague:
Feel free, it's Hack Proof. I trust AI's codes, \o/
```

Through this project we will guide you through exploiting 4 types of vulnerabilities which could occur within a web app.

You should have:
- Pre-installed Kali Linux (or use a sandbox)
- Access to our network (through OpenVPN or sandbox)
- Web browser (we recommend Firefox)
- Terminal (for curl and sqlmap)

### Warming Up
Get a target machine.

Endpoint: http://web0x00.hbtn/login

Append to your hosts file the domain `web0x00.hbtn` pointing to the target machine IP:
```bash
sudo bash -c "echo '<Target_IP> web0x00.hbtn' >> /etc/hosts"
```

Test your connectivity:

Via terminal:
```bash
curl http://web0x00.hbtn
```

Via browser:
- Visit http://web0x00.hbtn

## Repo
- GitHub repository: holbertonschool-cyber_security
- Directory: web_application_security/0x00_web_fundamentals
- File: README.md
