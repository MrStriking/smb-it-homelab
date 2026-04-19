# Network & Infrastructure


## Overview

All virtual machines run on VMware Workstation on a single laptop. Network communication between VMs is handled through VMware's Host-only virtual network, with pfSense acting as the gateway and firewall for all internal traffic. All VM traffic routes through pfSense on 192.168.10.1 before reaching the internet via VMware's NAT adapter.


## Network Design

| Device | Role | IP | Network Adapter |
|---|---|---|---|
| pfSense | Firewall/Gateway | WAN: DHCP, LAN: 192.168.10.1 | NAT (WAN) + Host-only (LAN) |
| Windows Server 2025 | Domain Controller | 192.168.10.10 | Host-only |
| Windows 11 | Client Workstation | 192.168.10.250 | Host-only |
| Ubuntu Server | SIEM + Helpdesk | 192.168.10.20 | Host-only |


## VM Specifications

| VM | RAM | Storage | CPU |
|---|---|---|---|
| Windows Server 2025 | 4GB | 60GB | 4 cores |
| Windows 11 | 4GB | 50GB | 4 cores |
| pfSense | 512MB | 20GB | 1 core |
| Ubuntu Server | 4GB | 50GB | 2 cores |
