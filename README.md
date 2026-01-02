# BGP Copilot Lab — NX-OS ↔ Cisco 8000v (IOS-XE)

**Author:** Anthony Edjenuwa  
**Domain:** Networking · BGP · Automation · Troubleshooting  

---

## Overview
This project demonstrates a production-style **eBGP adjacency validation and health reporting workflow**
between a **Cisco NX-OSv switch** (data-centre role) and a **Cisco 8000v IOS-XE router** (WAN/edge role).

The lab mirrors real-world operational practices used by NOCs, network engineers, and SOC teams
to verify BGP stability, confirm route exchange, and generate structured health reports.

---

## What This Lab Demonstrates
- eBGP adjacency establishment (NX-OS ↔ IOS-XE)
- Loopback /32 route advertisement and learning
- Control-plane and data-plane verification
- Deterministic JSON health reporting
- Optional AI-generated commentary (non-authoritative)

---

## Topology Summary
- **NX-OSv Switch**
  - ASN: 65001
  - Transit IP: 10.0.0.1/30
  - Loopback: 1.1.1.1/32

- **Cisco 8000v (IOS-XE)**
  - ASN: 65002
  - Transit IP: 10.0.0.2/30
  - Loopback: 2.2.2.2/32
  - WAN: DHCP (internet reachability)

- **Ubuntu Automation Host**
  - Subnet: 192.168.10.0/24
  - Default GW: 192.168.10.1
  - Used for validation and reporting

A labelled topology diagram is provided in the `assets/` directory.

---

## API Disclosure (Important)
Any AI API endpoint used during experimentation is intentionally **excluded** from this repository.

> **[API excluded by author — insert your endpoint here]**

The project is designed so that:
- Core health reporting is **deterministic**
- AI output is **optional and non-authoritative**
- No sensitive endpoints or credentials are exposed

---

## Repository Structure
```text
bgp-copilot-lab/
├── README.md
├── assets/
│   └── bgp-ai-labelled-side.png
├── scripts/
│   ├── local_bgp_report.py
│   ├── ai_comment.py
│   └── call_ai.py
├── outputs/
│   └── bgp_report.json
├── docs/
│   └── payload_examples.json

