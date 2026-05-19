# 0x01 - AD Basics And Concepts

## Overview
This module covers fundamental Active Directory (AD) concepts and basic reconnaissance techniques. You'll learn how to query and enumerate Active Directory domain objects to extract critical information.

## Learning Objectives

✅ Understand Active Directory structure and domain objects  
✅ Perform domain enumeration using various tools  
✅ Extract both standard and non-standard attributes  
✅ Identify and locate hidden information in domain objects  
✅ Document reconnaissance findings  

## Challenge 0: Domain Reconnaissance - Extracting Core Domain Information

### Objective
Every Active Directory environment exposes fundamental information through its root domain object. Your goal is to:
- Query the Active Directory domain object
- Inspect both standard and non-standard attributes
- Identify the attribute containing the hidden flag

### Key Concepts

#### Active Directory Domain Structure
```
Domain Root (CN=...)
├── Users
├── Computers
├── Groups
├── Organizational Units (OUs)
└── Other Objects
```

#### Standard vs Non-Standard Attributes
- **Standard Attributes**: name, description, distinguishedName, mail, etc.
- **Non-Standard Attributes**: Custom attributes added by administrators (e.g., extensionAttribute1-15, custom properties)

### Tools Required

#### 1. PowerShell (Windows)
```powershell
# Basic domain query
Get-ADDomain

# Query with all properties
Get-ADDomain | Select-Object *

# Query specific property
Get-ADDomain -Property * | Select-Object -Property distinguishedName, description
```

#### 2. ldapsearch (Linux/Mac)
```bash
# Basic LDAP query
ldapsearch -H ldap://domain_controller -x -b "DC=domain,DC=com" -s base

# Query with specific attributes
ldapsearch -H ldap://domain_controller -x -b "DC=domain,DC=com" -s base "*" "+"

# Save to file
ldapsearch -H ldap://domain_controller -x -b "DC=domain,DC=com" -s base "*" "+" > domain_dump.ldif
```

#### 3. ADExplorer (Windows Sysinternals)
- GUI tool for browsing Active Directory
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
