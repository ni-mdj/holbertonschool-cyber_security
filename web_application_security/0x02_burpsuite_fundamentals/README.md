# Burp Suite Fundamentals

## Description
Set up Burp Suite Community Edition to intercept web traffic, install the Burp CA certificate, and inspect TLS certificate details to extract flags.

## Tasks Overview
1. Install Burp Suite Community Edition.
2. Configure the proxy listener (default `127.0.0.1:8080`).
3. Configure a browser to route traffic through Burp.
4. Install the Burp CA certificate to avoid HTTPS warnings.
5. Add a hostname resolution override for `web0x02.hbtn` in Project options.
6. Browse the target through Burp and inspect Server TLS certificate details.

## Project Files
- `0-flag.txt`: flag for task 0.
- `1-flag.txt`: flag for task 1.
- `2-flag.txt`: flag for task 2.
- `3-flag.txt`: flag for task 3.
- `4-flag.txt`: flag for task 4.
- `5-flag.txt`: flag for task 5.
- `6-flag.txt`: flag for task 6.

## Notes
- Ensure Intercept is OFF when loading pages unless a task requires interception.
- Only test against targets you are authorized to access.

## Repo
- GitHub repository: holbertonschool-cyber_security
- Directory: `web_application_security/0x02_burpsuite_fundamentals`
- File: `README.md`
