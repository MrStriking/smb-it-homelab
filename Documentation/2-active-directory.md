# Active Directory


## Overview

Windows Server 2025 is configured as the domain controller for the lab domain `lab.local`. It provides Active Directory, DNS, and DHCP services for the internal network.


## Domain Details

| Setting | Value |
|---|---|
| Domain Name | lab.local |
| Domain Controller | DC01 |
| DNS Server | 192.168.10.10 |
| DHCP Scope | 192.168.10.100 — 192.168.10.200 |
| DHCP Gateway | 192.168.10.1 |


## Organisational Units and Users

<img width="275" height="677" alt="image" src="https://github.com/user-attachments/assets/c5436fd0-00ff-47dc-834e-77d0cb8a6f47" />


## Group Policies

Configured basic rules according to OUs such as minimal restriction to the IT OU, and control panel restriction to the HR OU. More policies were also configured for the domain for security reasons and compliance (more details in the Wazuh section).


## Windows 11 Client

The Windows 11 VM is joined to `lab.local` and configured with a static IP of 192.168.10.250. Domain users can log in using `lab\username` credentials, authenticated by the DC.
