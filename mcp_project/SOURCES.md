# Sources

Sources checked November 14, 2026. No website is accessed by the experiment.

## Course files

The starting server, notebook, 12 knowledge-base sections, and 11 expected service records came from the [IT7075 07_MCP folder](https://github.com/li2cc/IT7075-Applied-AI-for-Cybersecurity/tree/main/07_MCP), including both lecture notebooks. The original `lookup_cve` function is unchanged. The completed notebook keeps Parts 1–7 and extends Part 8. Practice stages use temporary copies so the final KB stays complete and precise.

The starter server file SHA was `3db17f85cce7741752e61f462d45dac874788197`; the starter notebook SHA was `00644ed5e571d25c7d3737f6959021514baa0adf`. These identify the downloaded course versions, not a file-integrity requirement for this project.

## Added or corrected knowledge

| Section | Source and what it supports |
| --- | --- |
| nginx 1.18.0 | [nginx security advisories](https://nginx.org/en/security_advisories.html): CVE-2021-23017, affected 0.6.18–1.20.0; fixed 1.20.1 and 1.21.0. [Vendor announcement](https://nginx.org/2021.html). Resolver configuration and DNS-forgery conditions matter. |
| PostgreSQL 9.6.24 | [PostgreSQL 9.6 security archive](https://www.postgresql.org/support/security/9.6/) marks the branch unsupported. [CWE-1104](https://cwe.mitre.org/data/definitions/1104.html) describes unmaintained components. [PostgreSQL CVE-2021-23214](https://www.postgresql.org/support/security/CVE-2021-23214/) lists 9.6.24 as FIXED, so this entry does not falsely report that CVE as active. |
| nginx 1.24.0 | [nginx CVE-2024-7347 announcement](https://mailman.nginx.org/pipermail/nginx-announce/2024/UUOCLLONPR6244YQYU65PO5LB7JDYCWM.html): MP4 module buffer overread, affected 1.5.13–1.27.0; fixed 1.26.2 and 1.27.1; module/configuration/file-processing conditions apply. |
| Apache httpd 2.4.50 | [Apache security advisories](https://httpd.apache.org/security/vulnerabilities_24.html): CVE-2021-42013 affects 2.4.49 and 2.4.50, fixed 2.4.51. Traversal and possible CGI code execution depend on configuration. CVE-2021-41773 alone covers 2.4.49, not 2.4.50. |
| MySQL 5.5 scope correction | [Debian security tracker](https://security-tracker.debian.org/tracker/CVE-2012-2122) and [Amazon Linux advisory](https://alas.aws.amazon.com/cve/html/CVE-2012-2122.html): CVE-2012-2122 was fixed in MySQL 5.5.24, so the course's 5.5.40 banner must not be marked vulnerable to it. The course heading is kept for the retrieval comparison; its body is corrected. |

## Other starter entries

The remaining course text is retained as teaching material for a controlled matching comparison, not as a current vulnerability feed. Relevant advisory records are [CVE-2011-2523](https://nvd.nist.gov/vuln/detail/CVE-2011-2523), [CVE-2018-15473](https://nvd.nist.gov/vuln/detail/CVE-2018-15473), [CVE-2021-41773](https://httpd.apache.org/security/vulnerabilities_24.html), [CVE-2021-44228](https://logging.apache.org/log4j/2.x/security.html), [CVE-2017-7494](https://www.samba.org/samba/security/CVE-2017-7494.html), [CVE-2017-0144](https://nvd.nist.gov/vuln/detail/CVE-2017-0144), [CVE-2015-3306](https://nvd.nist.gov/vuln/detail/CVE-2015-3306), [CVE-2014-0160](https://nvd.nist.gov/vuln/detail/CVE-2014-0160), and [CVE-2012-1823](https://nvd.nist.gov/vuln/detail/CVE-2012-1823). Redis and Telnet entries describe configuration/protocol risks, not a single CVE. Banner matching cannot establish patch status, vendor backports, module settings, or exploitation. Old remediation versions in inherited text are historical; use current vendor-supported packages for real decisions.

## MCP concepts and implementation

- [MCP architecture, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/architecture)
- [MCP initialization, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle)
- [MCP transports, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

The project uses the course's MCP 1.x client style and was executed with `mcp==1.30.0` and Python 3.12.14. A server process is a communication boundary, not an operating-system security sandbox. Tool descriptions and KB content are information to inspect, not trusted instructions. The port policy and host addresses are invented lab data, not an organizational policy.

## Measurement notes

The four buckets measure agreement with expected KB sections. Missing local evidence is not a clean bill of health. Part 5 uses the original expected values; Part 6 uses updated expected sections for nginx and PostgreSQL. This avoids counting newly added knowledge against the starter's old null expectations. The custom port tool is scored separately by expected port status. The vague-heading experiment runs in a temporary server/KB directory and leaves the submitted KB precise.
