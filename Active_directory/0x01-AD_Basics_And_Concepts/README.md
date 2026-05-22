# 0x01 - AD Basics And Concepts

## 📋 Module Overview

This comprehensive module dives deep into **Active Directory (AD) architecture** and reconnaissance techniques. Active Directory is the backbone of identity and access management in over 90% of enterprise environments, making it the **primary target for attackers**. This module teaches you how to enumerate, analyze, and exploit AD environments like a red teamer would.

### Why Active Directory Matters
- 🏢 Used in 90%+ of enterprises globally
- 🎯 #1 target for ransomware and APT actors
- 🔑 Gateway to privilege escalation and lateral movement
- 💼 Controls access to critical business resources
- ⚠️ Misconfiguration is rampant in real environments

## 🎯 Learning Objectives

By completing this module, you will be able to:

✅ **Explain Active Directory fundamentals** - Structure, domains, and trust relationships  
✅ **Understand authentication & authorization** - How AD verifies and authorizes users  
✅ **Enumerate domain information** - Query DC objects, users, groups, GPOs  
✅ **Identify domain attributes** - Standard vs. non-standard/custom attributes  
✅ **Extract hidden information** - Locate flags and sensitive data in AD objects  
✅ **Document reconnaissance findings** - Create professional reports from AD enumeration  
✅ **Identify misconfigurations** - Spot security weaknesses in AD setup  
✅ **Prepare for exploitation** - Understand attack vectors for future modules  

## 📚 Prerequisites & Setup

### Required Knowledge
- Basic networking (TCP/IP, DNS)
- Understanding of LDAP protocol
- Command-line proficiency (Bash/PowerShell)
- Basic Windows Server concepts

### Required Infrastructure
- **Windows Server 2019** - Domain Controller (DC)
- **Windows 11 Enterprise** - Member workstation
- **Kali Linux** - Attacker machine
- All VMs on the **same virtual network**
- **Credentials**: labuser / P@ssw0rd123!

### Tools to Install
```bash
# On Kali Linux / Mac
sudo apt-get install -y ldap-utils nmap smbclient
# or on Mac:
brew install openldap nmap
```

## 📖 Key Concepts You Need to Know

### 1. What is Active Directory?
Active Directory is Microsoft's **directory service** for Windows networks. Think of it as a phonebook for your company's IT infrastructure - it stores and manages:
- **Users** - Employee accounts
- **Computers** - Workstations and servers
- **Groups** - Collections of users for permission management
- **Group Policy Objects (GPOs)** - Configuration settings
- **Organizational Units (OUs)** - Logical containers for organizing objects
- **Resources** - Printers, shared folders, databases, etc.

### 2. Domain vs Forest
```
Forest (company.com)
├── Domain 1: corp.company.com
│   ├── OUs
│   ├── Users
│   ├── Computers
│   └── Groups
└── Domain 2: dev.company.com
    ├── OUs
    ├── Users
    ├── Computers
    └── Groups
```

### 3. Domain Controllers (DCs)
- Windows Server machines that **host and manage Active Directory**
- Store the AD database (ntds.dit file)
- Authenticate users and computers
- Replicate AD data between DCs
- Listen on **LDAP (port 389)** and **Kerberos (port 88)**

### 4. Authentication vs Authorization
| Aspect | Definition | Example |
|--------|-----------|---------|
| **Authentication** | "Who are you?" - Verifying identity | User enters username/password |
| **Authorization** | "What can you do?" - Granting permissions | User can access File Share A but not B |

### 5. LDAP (Lightweight Directory Access Protocol)
- Protocol for querying and modifying AD objects
- Default port: **389** (unencrypted) or **636** (SSL/TLS)
- Uses **Distinguished Names (DN)** to identify objects
- Example DN: `CN=Administrator,CN=Users,DC=lab,DC=local`

### 6. Domains and Trust Relationships
```
parent.local (Parent Domain)
    ↕ (Two-way trust)
child.parent.local (Child Domain)

company.com (Domain A)
    ↕ (External trust)
partner.com (Domain B)
```

## 🔍 Active Directory Structure Deep Dive

### Distinguished Names (DN) Format
```
CN=John Doe,OU=Users,OU=Sales,DC=company,DC=com
│   │                  │      │                  │
│   │                  │      │                  └─ Domain Components
│   │                  │      └─ Organizational Units (OUs)
│   │                  └─ Organizational Unit
│   └─ Common Name (actual object name)
└─ Component type (CN, OU, DC, etc.)
```

### LDAP Components
| Component | Full Name | Example |
|-----------|-----------|---------|
| **CN** | Common Name | CN=Administrator |
| **OU** | Organizational Unit | OU=Sales |
| **DC** | Domain Component | DC=company |
| **C** | Country | C=US |
| **ST** | State/Province | ST=California |
| **L** | Locality | L=San Francisco |
| **O** | Organization | O=Company Inc |

### AD Object Types
```
Domain Root
├── Users Container
│   ├── Administrator (user)
│   ├── Guest (user)
│   └── Domain Users (group)
├── Computers Container
│   ├── DESKTOP-ABC123 (computer)
│   └── SERVER-XYZ789 (computer)
├── Organizational Units (OUs)
│   ├── IT
│   ├── Sales
│   ├── HR
│   └── Finance
├── Groups
│   ├── Domain Admins (group)
│   ├── Domain Users (group)
│   └── Enterprise Admins (group)
└── Group Policy Objects (GPOs)
    ├── Default Domain Policy
    └── Custom Policies
```

## 🛠️ Tools Reference

### 1. ldapsearch (Linux/Mac/Kali) ⭐ PRIMARY TOOL

**Installation:**
```bash
# Kali/Ubuntu/Debian
sudo apt-get install -y ldap-utils

# macOS
brew install openldap
```

**Basic Queries:**
```bash
# Discover domain naming context
ldapsearch -H ldap://192.168.1.100 -x -b "" -s base namingContexts

# Query domain object (standard attributes only)
ldapsearch -H ldap://192.168.1.100 -x -b "DC=lab,DC=local" -s base

# Query domain object (ALL attributes - standard + non-standard) 🔑 KEY QUERY
ldapsearch -H ldap://192.168.1.100 -x -b "DC=lab,DC=local" -s base "*" "+"

# Query all users
ldapsearch -H ldap://192.168.1.100 -x -b "DC=lab,DC=local" -s sub "(objectClass=user)"

# Query all groups
ldapsearch -H ldap://192.168.1.100 -x -b "DC=lab,DC=local" -s sub "(objectClass=group)"

# Query with credentials
ldapsearch -H ldap://192.168.1.100 -x -D "cn=Administrator,cn=Users,DC=lab,DC=local" \
  -w "P@ssw0rd123!" -b "DC=lab,DC=local" -s base "*" "+"

# Save results to file
ldapsearch -H ldap://192.168.1.100 -x -b "DC=lab,DC=local" -s base "*" "+" > ad_dump.ldif

# Search for specific attribute
ldapsearch -H ldap://192.168.1.100 -x -b "DC=lab,DC=local" -s base | grep -i extensionAttribute
```

### 2. PowerShell (Windows) - Active Directory Module

**Installation:**
```powershell
# Install RSAT (Remote Server Administration Tools)
Add-WindowsCapability -Online -Name "Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0"

# Import AD module
Import-Module ActiveDirectory
```

**Key Commands:**
```powershell
# Get domain information
Get-ADDomain

# Get ALL domain properties
Get-ADDomain -Property *

# Get specific properties
Get-ADDomain -Property * | Select-Object -Property distinguishedName, description, extensionAttribute*

# Get all users
Get-ADUser -Filter * -Properties *

# Get all groups
Get-ADGroup -Filter * -Properties *

# Get all computers
Get-ADComputer -Filter * -Properties *

# Search for specific user
Get-ADUser -Identity "Administrator" -Properties *

# Export to CSV for analysis
Get-ADDomain -Property * | Export-Csv -Path domain_info.csv -NoTypeInformation
```

### 3. Nmap - Network Scanning

**Key Commands:**
```bash
# Scan for LDAP service (port 389)
nmap -p 389 192.168.1.100

# Scan for Kerberos (port 88)
nmap -p 88 192.168.1.100

# Scan for common AD ports
nmap -p 88,389,445,636 192.168.1.100

# OS detection with AD ports
nmap -O -p 88,389,445 192.168.1.100
```

### 4. smbclient - SMB Shares

```bash
# List shares
smbclient -L //192.168.1.100 -U administrator

# Connect to share
smbclient //192.168.1.100/C$ -U administrator

# Null session enumeration
smbclient -L //192.168.1.100 -U "" -N
```

## 📋 Challenge 0: Domain Reconnaissance - Extracting Core Domain Information

### 🎯 Challenge Objective

Every Active Directory environment exposes fundamental information through its root domain object. Your mission is to:

1. ✅ **Query** the Active Directory domain object
2. ✅ **Inspect** both standard and non-standard attributes
3. ✅ **Identify** the attribute containing the hidden flag
4. ✅ **Extract** and document the flag

**Hint:** Standard domain queries do not return all available attributes. Some fields require **explicit property requests** to be visible.

### 🔑 Key Challenge Points

- Standard LDAP queries miss hidden attributes
- The **`"+"`** flag in ldapsearch reveals operational/custom attributes
- Flags are typically hidden in non-standard attributes like:
  - `extensionAttribute1-15`
  - `description`
  - `adminDescription`
  - `info`
  - Custom schema attributes

### 📊 Standard vs Non-Standard Attributes

| Attribute Type | Description | Visible By Default? | Examples |
|---|---|---|---|
| **Standard** | Core AD attributes | ✅ Yes | name, mail, phone |
| **Operational** | System attributes | ❌ No (need +) | createTimeStamp, modifyTimeStamp |
| **Extension** | Custom attributes | ❌ No (need +) | extensionAttribute1-15 |
| **Custom Schema** | Organization-specific | ❌ No (need +) | Any custom attribute |
- View all attributes without special parameters
- Search and filter capabilities

### Reconnaissance Methodology

#### Step 1: Connect to Domain
```powershell
# Test connectivity
Test-NetConnection -ComputerName domain_controller -Port 389

# Or using LDAP
ldapsearch -H ldap://domain_controller -x -b "DC=domain,DC=com" -s base objectClass=*
```

#### Step 2: Query Domain Object
```powershell
# Get all domain information
$domain = Get-ADDomain
$domain | Format-List *
```

#### Step 3: Enumerate All Attributes
```powershell
# Request all attributes explicitly
Get-ADDomain -Property * | Select-Object *

# Export to CSV for analysis
Get-ADDomain -Property * | Export-Csv -Path domain_attributes.csv
```

#### Step 4: Search for Hidden Attributes
```powershell
# Look for non-standard properties
Get-ADDomain -Property * | Select-Object -Property * | 
    Where-Object {$_ -match "FLAG|flag|SECRET|secret|custom"}

# Check extension attributes
Get-ADDomain -Property * | Select-Object -Property extensionAttribute*
```

#### Step 5: Extract and Verify Flag
Once you've found the flag:
1. Document the attribute name
2. Record the exact flag value
3. Explain why this attribute was not visible in standard queries
4. Submit findings

### Common Hidden Attributes

| Attribute | Description |
|-----------|------------|
| extensionAttribute1-15 | Custom attributes for storing data |
| description | Often contains additional information |
| comments | Additional metadata |
| adminDescription | Admin-specific notes |
| info | General information field |
| location | Physical location |
| department | Department information |
| company | Company/organization name |

### Hints

💡 **Hint 1**: Standard domain queries do not return all available attributes. Some fields require explicit property requests to be visible.

💡 **Hint 2**: Use `-Property *` in PowerShell or request both "*" and "+" in LDAP to get all attributes.

💡 **Hint 3**: Check the extensionAttribute fields - they are often used for custom data.

💡 **Hint 4**: The flag might not be in obvious places like "description" or "comments".

### Expected Output

```
Domain Name: domain.local
Distinguished Name: DC=domain,DC=com
Forest Functional Level: 2016
Domain Functional Level: 2016

Hidden Flag Found!
Attribute: [ATTRIBUTE_NAME]
Value: FLAG{AD_Domain_Reconnaissance_Complete}
```

### Success Criteria

✅ Successfully connected to Active Directory  
✅ Retrieved domain object information  
✅ Located non-standard attributes  
✅ Extracted the hidden flag  
✅ Documented the reconnaissance methodology  

### Troubleshooting

#### Connection Issues
```powershell
# Verify domain controller is reachable
nslookup domain.com
ping domain_controller

# Check LDAP port
Test-NetConnection -ComputerName domain_controller -Port 389
```

#### Permission Issues
```powershell
# May require domain credentials
$credential = Get-Credential
Get-ADDomain -Credential $credential -Property *
```

#### No Results
- Ensure you're using `-Property *` to get all attributes
- Try with administrative credentials
- Verify domain controller hostname is correct

### Files in This Challenge

- **0-flag.txt**: Instructions and framework for the challenge
- **README.md**: This documentation file

### Resources

- [Microsoft Active Directory Documentation](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started-with-active-directory-domain-services)
- [PowerShell Get-ADDomain](https://docs.microsoft.com/en-us/powershell/module/activedirectory/get-addomain)
- [LDAP Query Basics](https://ldapwiki.com/wiki/Active%20Directory%20Query%20Examples)
- [AD Reconnaissance Techniques](https://adsecurity.org/)

### Next Steps

Once you complete this challenge:
1. Review AD security best practices
2. Explore user and group enumeration
3. Study permission delegation in AD
4. Practice exploitation techniques

---

**Author**: Security Team  
**Last Updated**: May 2026  
**Difficulty**: Beginner  
**Time Estimate**: 30-45 minutes
