# Known Issues & Troubleshooting

This document records issues encountered during the lab build, and how they were resolved or worked around. I thought I'd include this section despite most issues not being ideally solved.

---

## 1. DHCP Not Serving Windows 11 Client

The Windows 11 VM set to DHCP received a `192.168.211.x` address from VMware's built-in DHCP rather than `192.168.10.x` from the DC. I confirmed that the DC DHCP scope was active, showing leases, and ran `ipconfig /release` and `ipconfig /renew`. I also confirmed that both VMs were on Host-only network. This issue might be due to VMware Host-only network broadcast behaviour occasionally preventing DHCP requests from reaching the DC. So, I had to assign a static IP address to the client workstation.

---

## 2. LDAP Query from Ubuntu to Active Directory

As mentioned in the Peppermint section, the ticket generator script failed to query the DC with several authentication protocols. I also got an invalidCredentials error at one point despite confirming everything was correct. So, I just went ahead with a script that doesn't assign users to each ticket. While not a major issue for a ticket generator script, LDAP is vital for other more serious scripts that require the retrieval on DC information from another device/vm.

---

## 3. SCA Policy Incompatibility with Windows Server 2025

When I attempted an SCA scan for the first time, I got an error message: `Skipping policy cis_win2022.yml: Check that the Windows platform is Windows Server 2022`. I modified the policy file on the agent to support 2025 version. The scan did eventually work, however the compliance checks are according to the 2022 server version as mentioned before, so the scan is most definitely misleading with some remediations not being possible on the 2025 server version.

---

## 4. Peppermint API Token Unavailable

The API token option in the Peppermint UI was greyed out, and it was needed for the ticket generator script. So, I included a get_token() function which authenticates the user returning a JWT token. Honestly, this is a better approach rather than hard coding in the token.

---
