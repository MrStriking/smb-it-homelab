# Peppermint Helpdesk


## Overview

Peppermint is an open source helpdesk and ticketing system deployed on the Ubuntu Server via Docker. It simulates the helpdesk function of a small business IT department, providing a ticket management interface for logging, tracking, and resolving IT issues.

<img width="1653" height="670" alt="image" src="https://github.com/user-attachments/assets/6cb91050-43ff-433c-b321-7fb113a18990" />


## Deployment

Peppermint is deployed using Docker Compose with a PostgreSQL database:

| Container | Role | Port |
|---|---|---|
| peppermint | Web application | 3000 |
| peppermint_postgres | Database | 5432 |

Accessible at: `http://192.168.10.20:3000`


## Ticket Automation

To get more realistic hands on practice with the ticketing system, I wrote a python script that would send a ticket every few minutes. The main idea was more to gain the knowledge of handling the ticket by commenting, escalating, and assigning to appropriate users rather than solving the actual complaints. I also researched the standards and protocols to dealing with clients via a ticketing system to fully unerstand the idea in a real life environment. The script (`ticket_generator.py`) does the following:
- Authenticates to Peppermint via REST API using JWT token
- Selects a random ticket scenario from a pool of realistic IT issues
- Randomly assigns priority (Low, Medium, High)
- Checks Peppermint is available before running
- Runs on a 30 minute cron schedule on the Ubuntu server


My initial idea for the script included dynamically pulling users from OUs to assign a client (HR, Finance,...) and an IT support to handle the issue for every ticket. However, their were NTLM/MD4 compatibility issues between the ldap3 Python library and newer OpenSSL versions on Ubuntu 24.04. Even with the more secure LDAPS, I kept getting the strongerAuthRequired error.
