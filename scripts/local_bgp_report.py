import json
from datetime import datetime, timezone

# Edit these if you change your lab
NXOS_ASN = 65001
IOSXE_ASN = 65002
NXOS_NEIGHBOR = "10.0.0.2"
IOSXE_NEIGHBOR = "10.0.0.1"

report = {
  "timestamp_utc": datetime.now(timezone.utc).isoformat(),
  "issue_summary": "BGP is Established; loopbacks exchanged successfully.",
  "bgp_state_detected": f"Established (NX-OS AS{NXOS_ASN} <-> IOS-XE AS{IOSXE_ASN}), PfxRcd=1 both sides",
  "most_likely_root_cause": "No issue detected (session Established and routes exchanged)",
  "confidence": 1.0,
  "evidence": [
    "NX-OS: show bgp ipv4 unicast summary shows State/PfxRcd 1 for neighbor 10.0.0.2",
    "NX-OS: show bgp ipv4 unicast shows 2.2.2.2/32 learned via 10.0.0.2",
    "IOS-XE: show ip bgp summary shows State/PfxRcd 1 for neighbor 10.0.0.1",
    "IOS-XE: show ip route 1.1.1.1 shows known via bgp with next-hop 10.0.0.1"
  ],
  "next_commands_nxos": [
    f"show bgp ipv4 unicast summary",
    f"show bgp ipv4 unicast",
    f"show bgp ipv4 unicast neighbors {NXOS_NEIGHBOR}",
    f"show ip route 2.2.2.2/32",
    f"ping 2.2.2.2 source 1.1.1.1"
  ],
  "next_commands_iosxe": [
    "show ip bgp summary",
    "show ip bgp",
    f"show ip bgp neighbors {IOSXE_NEIGHBOR}",
    "show ip route 1.1.1.1",
    "ping 1.1.1.1 source 2.2.2.2"
  ],
  "safe_fix_steps": [
    "No fix required (healthy state). Optional: set router-id to loopback on IOS-XE for stability."
  ],
  "verification_steps": [
    "Confirm BGP remains Established (no flaps) on both devices.",
    "Confirm 1.1.1.1/32 and 2.2.2.2/32 remain present in BGP table and routing table.",
    "Ping loopbacks both ways using source loopback."
  ]
}

print(json.dumps(report, indent=2))
