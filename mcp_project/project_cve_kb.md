# vsftpd 2.3.4
The vsftpd 2.3.4 FTP server (commonly seen on port 21) shipped with a malicious backdoor introduced into the source distribution. Connecting with a username ending in ":)" opens a command shell on TCP port 6200, granting remote command execution as root. Tracked as CVE-2011-2523. Severity: critical. Remediation: upgrade to a clean, vendor-verified vsftpd build and verify package checksums; never run software from unverified mirrors.

# OpenSSH 7.2p2
OpenSSH versions before 7.7 (including the 7.2 series often seen on port 22) are affected by a username enumeration weakness, CVE-2018-15473. By measuring response timing differences to malformed authentication requests, an attacker can determine which usernames exist on the system, aiding password-guessing and spear-phishing. Severity: medium. Remediation: upgrade OpenSSH to 7.7 or later, enforce key-based authentication, and rate-limit authentication attempts with fail2ban.

# Apache httpd 2.4.49
Apache HTTP Server 2.4.49 (port 80/443) contains a path-traversal flaw, CVE-2021-41773. A crafted URL using encoded "../" sequences can read files outside the document root, and when mod_cgi is enabled it escalates to remote code execution. Severity: critical. Remediation: upgrade to Apache 2.4.51 or later, disable directory aliasing you do not need, and ensure "require all denied" is set on the filesystem root.

# Apache Log4j 2.14
Applications using Apache Log4j 2 versions 2.0-beta9 through 2.14.1 are vulnerable to Log4Shell, CVE-2021-44228. If attacker-controlled text is logged, a JNDI lookup string such as "${jndi:ldap://...}" causes the server to fetch and execute remote code. This often surfaces through web services on ports 80/443/8080. Severity: critical. Remediation: upgrade Log4j to 2.17.1 or later, set log4j2.formatMsgNoLookups=true as a stopgap, and block outbound LDAP/RMI from servers.

# Samba 3.5.0
Samba file-sharing services (ports 139/445) from 3.5.0 up to 4.6.4 are vulnerable to CVE-2017-7494, nicknamed SambaCry. An authenticated client that can write to a share can upload and trigger a shared library, achieving remote code execution on the server. Severity: critical. Remediation: patch Samba to a fixed release, add "nt pipe support = no" to smb.conf as mitigation, and restrict share write access.

# Microsoft SMBv1
Windows hosts exposing SMBv1 (port 445) are vulnerable to EternalBlue, CVE-2017-0144, addressed by bulletin MS17-010. A malformed SMBv1 packet causes a buffer overflow leading to remote code execution; this was the propagation vector for the WannaCry and NotPetya worms. Severity: critical. Remediation: apply MS17-010, disable SMBv1 entirely, and block port 445 at the network perimeter.

# ProFTPD 1.3.5
ProFTPD 1.3.5 (port 21) with the mod_copy module enabled is vulnerable to CVE-2015-3306. The SITE CPFR and SITE CPTO commands can be used without authentication to copy files anywhere the daemon can write, enabling attackers to plant a web shell or read sensitive files. Severity: high. Remediation: upgrade ProFTPD, disable mod_copy unless required, and run the FTP daemon under a restricted account.

# OpenSSL 1.0.1
Services using OpenSSL 1.0.1 through 1.0.1f for TLS (ports 443, 993, 995, and others) are vulnerable to Heartbleed, CVE-2014-0160. A malformed TLS heartbeat request makes the server return up to 64 KB of process memory per request, which can leak private keys, session cookies, and credentials. Severity: critical. Remediation: upgrade OpenSSL to 1.0.1g or later, revoke and reissue affected certificates and keys, and force user password resets.

# MySQL 5.5
Historical scope note: CVE-2012-2122 affected MySQL 5.5 before 5.5.24 on certain builds, where an incorrect password could pass authentication because of a faulty comparison result. The lab banner MySQL 5.5.40 is later than that fix, so this CVE must not be reported as an active vulnerability for that banner. This family-level heading is retained for the course retrieval comparison, not as evidence that 5.5.40 is vulnerable. Review the exact build and use a supported database release. Source: https://security-tracker.debian.org/tracker/CVE-2012-2122

# Redis 4.0
Redis instances (port 6379) left without authentication and reachable over the network can be abused for remote code execution. An attacker writes a malicious module or crafted RDB/SSH key file via unauthenticated commands and loads it. There is no single CVE; this is a configuration weakness widely exploited in the wild. Severity: critical. Remediation: require a strong "requirepass", bind Redis to localhost or a private interface, enable protected-mode, and disable the MODULE and CONFIG commands.

# PHP-CGI
Web servers running php-cgi (ports 80/443) are vulnerable to CVE-2012-1823, an argument-injection flaw. Query strings beginning with "?-" are passed to the PHP binary as command-line switches, allowing source disclosure or remote code execution. Severity: critical. Remediation: upgrade PHP, use PHP-FPM instead of php-cgi, and add a web-server rule that rejects request strings starting with a dash.

# Telnet service
A telnet service (port 23) transmits all data, including usernames and passwords, in cleartext with no encryption. Anyone able to observe the traffic can capture credentials, and telnet is frequently left enabled with default credentials on routers, switches, and IoT devices. Severity: high. Remediation: disable telnet entirely and replace it with SSH; if a serial-console fallback is required, isolate it on a dedicated management network.

# nginx 1.18.0
CVE-2021-23017 is a one-byte memory overwrite in the nginx DNS resolver. The upstream affected range is 0.6.18 through 1.20.0, which includes 1.18.0; fixed releases include 1.20.1 and 1.21.0. Exploitation depends on use of the resolver directive and an attacker able to forge a DNS response. Review configuration and vendor backports before treating a banner as vulnerable. Update to a supported, fixed package. Source: https://nginx.org/en/security_advisories.html

# PostgreSQL 9.6.24
PostgreSQL 9.6 is an unsupported upstream branch. CWE-1104 describes the risk of using unmaintained third-party components; plan a migration to a supported release. Historical CVE-2021-23214 involved SQL injection by a man-in-the-middle during certain SSL authentication setups, but 9.6.24 is a FIXED release for that CVE, not an affected one. This entry is a lifecycle warning and fixed-version context, not a claim that this banner has that vulnerability. Sources: https://www.postgresql.org/support/security/9.6/ and https://www.postgresql.org/support/security/CVE-2021-23214/ and https://cwe.mitre.org/data/definitions/1104.html

# nginx 1.24.0
CVE-2024-7347 is a buffer overread in ngx_http_mp4_module. The upstream affected range is 1.5.13 through 1.27.0, including 1.24.0; fixes include 1.26.2 and 1.27.1. The module must be built and configured for MP4 processing, and the attacker must be able to make the server process a crafted media file. A banner alone does not establish those conditions. Check the build and configuration, then use a supported, fixed package. Source: https://mailman.nginx.org/pipermail/nginx-announce/2024/UUOCLLONPR6244YQYU65PO5LB7JDYCWM.html

# Apache httpd 2.4.50
CVE-2021-42013 affects Apache HTTP Server 2.4.49 and 2.4.50 and was fixed in 2.4.51. An incomplete path-normalization fix allowed traversal outside Alias-like directories when access controls did not deny access; CGI enabled on those paths could allow code execution. Review configuration and install a supported, fixed release. The older CVE-2021-41773 entry for 2.4.49 alone is not the correct advisory for a 2.4.50 banner. Source: https://httpd.apache.org/security/vulnerabilities_24.html
