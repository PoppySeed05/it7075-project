"""Offline MCP lab: simulated hosts, two CVE lookups, and a port-policy check.

The notebook launches this server as a separate process over stdio. No tool
sends network packets, runs a shell command, or changes a host. The original
lookup_cve function is retained verbatim for the comparison.
"""
import re
from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("cyber-recon-project", log_level="WARNING")


def _kb_path():
    return Path(__file__).resolve().with_name("project_cve_kb.md")


def _load_kb_sections():
    """Keep the starter's section parser; headings contain product and version."""
    sections = {}
    for chunk in _kb_path().read_text(encoding="utf8").split("#"):
        chunk = chunk.strip()
        if chunk:
            sections[chunk.splitlines()[0].strip()] = chunk
    return sections


_SIMULATED_HOSTS = {
    "10.0.0.5": [
        "21/tcp   open  ftp      vsftpd 2.3.4",
        "22/tcp   open  ssh      OpenSSH 7.2p2 Ubuntu",
        "80/tcp   open  http     Apache httpd 2.4.49",
    ],
    "10.0.0.8": [
        "139/tcp  open  netbios-ssn Samba smbd 3.5.0",
        "3306/tcp open  mysql    MySQL 5.5.40",
    ],
    "10.0.0.12": [
        "23/tcp   open  telnet   Linux telnetd",
        "443/tcp  open  ssl/http Apache httpd 2.2.8 (OpenSSL 1.0.1)",
        "6379/tcp open  redis    Redis key-value store 4.0.9",
    ],
    "10.0.0.20": [
        "21/tcp   open  ftp      ProFTPD 1.3.5",
        "80/tcp   open  http     nginx 1.18.0",
        "5432/tcp open  postgres PostgreSQL 9.6.24",
    ],
    # My host: one covered banner and two initially missing versions.
    "10.0.0.30": [
        "22/tcp   open  ssh      OpenSSH 7.2p2 Ubuntu",
        "80/tcp   open  http     nginx 1.24.0",
        "8080/tcp open  http     Apache httpd 2.4.50",
    ],
}


@mcp.tool()
def port_scan(target: str) -> str:
    """Read canned nmap-style banners for one known simulated lab IP.

    target must exactly match an IP returned by list_targets. Returns a text
    header and open TCP ports with service names and versions. Unknown targets
    return a tool error, not a clean scan. No real scan or network traffic occurs.
    A banner is lab data, not proof of a vulnerability or of a safe host.
    """
    if target not in _SIMULATED_HOSTS:
        raise ValueError("Unknown simulated target; call list_targets first.")
    header = f"Nmap scan report for {target}\nPORT     STATE SERVICE  VERSION"
    return header + "\n" + "\n".join(_SIMULATED_HOSTS[target])


@mcp.tool()
def list_targets() -> str:
    """List the five fictional IPs accepted by this offline lab's host tools."""
    return "Known simulated targets: " + ", ".join(_SIMULATED_HOSTS)


@mcp.tool()
def lookup_cve(service: str) -> str:
    """Look up known vulnerabilities for a service or product name (e.g.
    'vsftpd 2.3.4', 'Apache 2.4.49') in the local knowledge base.

    THE LECTURE VERSION -- left here unchanged so you can measure against it.
    It matches when two or more words of the query appear anywhere in a section,
    which is why it both misses services it knows and answers with the wrong
    version. Part 7 shows you exactly where.
    """
    sections = _load_kb_sections()
    query = service.lower()
    tokens = [t for t in query.replace("/", " ").split() if t]
    hits = [body for title, body in sections.items()
            if title.lower() in query or sum(tok in (title + " " + body).lower()
                                             for tok in tokens) >= 2]
    return "\n\n".join(hits) if hits else f"No known CVEs for '{service}' in the knowledge base."


@mcp.tool()
def lookup_cve_v2(service: str) -> str:
    """Read local KB sections whose heading product and version match a banner.

    service is a product/version banner, for example 'nginx 1.24.0'. The first
    heading word must occur in the banner; the heading's version string must
    also occur if present. A versionless heading matches any version of that
    product. This is substring matching, not a semantic version-range check.
    Returns matching Markdown sections or 'No known CVEs ... in the knowledge
    base'. No match means missing local evidence, not a safe service. Entries
    can describe historical fixes or configuration risks. Verify applicability
    with the cited source; the tool does not confirm exploitability.
    """
    sections = _load_kb_sections()
    text = service.lower()
    hits = []
    for title, body in sections.items():
        product = title.lower().split()[0]
        # A word boundary avoids treating the 4 inside Log4j as a version.
        version = re.search(r"\b\d[\d.p]*", title)
        # TODO 1 completed: require product and (when supplied) version.
        match = product in text and (version is None or version.group() in text)
        if match:
            hits.append(body)
    return "\n\n".join(hits) if hits else f"No known CVEs for '{service}' in the knowledge base."


@mcp.resource("kb://cve")
def cve_kb() -> str:
    """Read the full local Markdown knowledge base, including historical context."""
    # TODO 2 completed: expose the file through an MCP resource URI.
    return _kb_path().read_text(encoding="utf8")


@mcp.tool()
def check_port_policy(target: str) -> dict:
    """Compare a known simulated host's TCP ports with a fictional lab policy.

    target must exactly match an IP returned by list_targets. The policy allows
    ports 22 and 443; every other open port is marked review_required. Returns
    target, policy_id, allowed_tcp_ports, per-service port/banner/status/reason,
    and summary counts. Unknown targets return a tool error.
    This read-only check uses canned banners. It sends no packets, changes no
    firewall rules, and does not determine whether a service is vulnerable.
    review_required means an analyst should review a lab-policy exception;
    allowed does not mean secure. The policy is an example, not a standard.
    """
    if target not in _SIMULATED_HOSTS:
        raise ValueError("Unknown simulated target; call list_targets first.")
    allowed_ports = {22, 443}
    services = []
    for line in _SIMULATED_HOSTS[target]:
        endpoint, state, service, banner = line.split(maxsplit=3)
        port_text, protocol = endpoint.split("/")
        port = int(port_text)
        allowed = port in allowed_ports
        services.append({
            "port": port, "protocol": protocol, "service": service,
            "banner": banner,
            "status": "allowed" if allowed else "review_required",
            "reason": "Port is in the lab allowlist." if allowed
                      else "Port is outside the lab allowlist; analyst review required.",
        })
    return {
        "target": target, "policy_id": "lab-management-v1",
        "allowed_tcp_ports": sorted(allowed_ports), "services": services,
        "summary": {
            "allowed": sum(s["status"] == "allowed" for s in services),
            "review_required": sum(s["status"] == "review_required" for s in services),
        },
        "limitations": "Simulated, read-only policy check; not a vulnerability verdict.",
    }


if __name__ == "__main__":
    # stdout belongs to the MCP protocol. Use stderr for any diagnostics.
    mcp.run(transport="stdio")
