# pfSense


## Overview

pfSense 2.8.1 is deployed as the network firewall and router for the lab environment. It sits between the VMware NAT interface (WAN) and the internal Host-only network (LAN), routing and filtering the traffic.

<img width="797" height="448" alt="image" src="https://github.com/user-attachments/assets/926d35ba-2cd1-42cf-9cd1-c0d65cd07aef" />


## Interface Configuration

| Interface | Type | IP |
|---|---|---|
| WAN (em0) | DHCP | Assigned by VMware NAT |
| LAN (em1) | Static | 192.168.10.1/24 |


## Firewall Rules

The following LAN rules were configured via pfSense gui:

| Rule | Protocol | Source | Destination | Port |
|---|---|---|---|---|
| Allow DNS to DC | TCP/UDP | LAN subnet | 192.168.10.10 | 53 |
| Allow internal traffic | Any | 192.168.10.0/24 | 192.168.10.0/24 | Any |
| Allow internet outbound | Any | LAN subnet | Any | Any |
| Block RDP to DC | TCP | Any | 192.168.10.10 | 3389 |

Then there's the implicit deny blocking all other traffic.


## Syslog Forwarding to Wazuh

pfSense was configured to forward all firewall logs to the Wazuh manager via syslog. This allows firewall events such as blocked connections and traffic patterns to appear alongside endpoint alerts in the Wazuh SIEM dashboard.
