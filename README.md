# Small Business IT Environment


## Introduction

The best way to actually learn and get familiar with IT and cybersecurity concepts, tools, and skills is to get hands on with them. So, I've decided to create a simple small business (SMB) IT environment on my laptop to learn what I can. It's nothing crazy or overly impressive, but it does demonstrate my newly gained knowledge and experience in the IT area.


## Overview

This lab simulates a small business IT environment running entirely on my laptop using VMware Workstation. It includes a domain controller, a domain-joined client workstation, a firewall, a SIEM, and a helpdesk ticketing system where all systems are connected and communicating as they would in a real SMB.


## IT Environment Summary

| Component | Technology | IP Address |
|---|---|---|
| Domain Controller | Windows Server 2025 | 192.168.10.10 |
| Client Workstation | Windows 11 | 192.168.10.250 |
| Firewall/Router | pfSense 2.8.1 | 192.168.10.1 |
| SIEM + Ticketing | Ubuntu Server 24.04 | 192.168.10.20 |


## Tools and Technologies Used

- **VMware Workstation**: hypervisor hosting all VMs.
- **Windows Server 2025**: Active Directory, DNS, DHCP.
- **Windows 11**: domain-joined client workstation.
- **pfSense**: firewall, routing, and network segmentation.
- **Wazuh**: SIEM, FIM, SCA, vulnerability detection.
- **Peppermint**: open source helpdesk ticketing system.
- **Docker**: deployment of Wazuh and Peppermint containers.


## Network Topology

```
Internet
    |
[pfSense] WAN: DHCP (VMware NAT)
    |      LAN: 192.168.10.1/24
    |
192.168.10.0/24 (Internal LAN)
    |
    |-- Windows Server 2025 (DC01)     192.168.10.10
    |-- Windows 11 (WIN11-CLIENT)      192.168.10.250
    |-- Ubuntu Server (ubuntu-srv)     192.168.10.20
              |-- Peppermint (port 3000)
              |-- Wazuh (Docker)
```


## Skills Demonstrated/Tackled

- Active Directory administration (users, OUs, Group Policy).
- Network and firewall configuration and management.
- SIEM deployment and log monitoring across multiple agents.
- File Integrity Monitoring and Security Configuration Assessment.
- Helpdesk ticketing system deployment and simulation.
- Linux server administration.


## Documentation

- [Network & Infrastructure](Documentation/1-network-topology.md)
- [Active Directory](Documentation/2-active-directory.md)
- [pfSense](Documentation/3-pfsense.md)
- [Wazuh SIEM](Documentation/4-wazuh-siem.md)
- [Peppermint Helpdesk](Documentation/5-peppermint-helpdesk.md)
- [Known Issues & Troubleshooting](Documentation/6-known-issues.md)
