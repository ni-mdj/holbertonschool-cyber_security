# SQLi / NoSQLi Injection Discovery

## Description
Identify vulnerable parameters in a web application by probing inputs for SQL injection behavior. The goal is to find the parameter that changes the response or triggers SQL errors, then record its name.

## Target
- Host: `web0x01.hbtn`
- Path: `/a3/sql_injection/`

## Suggested Approach
- Add `web0x01.hbtn` to `/etc/hosts` with the lab IP.
- Browse the application and note URL parameters and form inputs.
- Test inputs with simple payloads such as `'` and `' OR '1'='1`.
- Observe changes in output or errors.
- Write the vulnerable parameter name to `0-vuln.txt`.

## Project Files
- `0-vuln.txt`: name of the vulnerable parameter.

## Notes
- Only test against targets you are authorized to access.

## Repo
- GitHub repository: holbertonschool-cyber_security
- Directory: `web_application_security/0x03_sql_nosql_injection`
- File: `README.md`
