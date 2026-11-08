# Sources

All twelve alerts are fictional examples written for this assignment. They are not copied employer logs or reports of actual incidents. Public sources below explain the alert types; the labels and supporting circumstances are judgments within the fictional scenarios. The draft was prepared with AI assistance and should be reviewed before submission.

| Alerts | Public source | What it helped describe |
| --- | --- | --- |
| M01, M07 | [MITRE ATT&CK T1486](https://attack.mitre.org/techniques/T1486/) | File encryption as a security signal. M07's approved exercise is invented classroom context. |
| M02 | [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/) | Exploitation of a public-facing service. No real vulnerability or CVE is claimed. |
| M03 | [MITRE ATT&CK T1098](https://attack.mitre.org/techniques/T1098/) | Account and permission changes. |
| M04, M12 | [MITRE ATT&CK T1621](https://attack.mitre.org/techniques/T1621/) | Misuse of MFA requests; M12 is an invented benign comparison involving a verified replacement phone. |
| M05 | [MITRE ATT&CK T1078](https://attack.mitre.org/techniques/T1078/) | Misuse of valid accounts, including accounts that should no longer be used. |
| M06 | [MITRE ATT&CK T1114.003](https://attack.mitre.org/techniques/T1114/003/) | Mail forwarding rules used to collect information. |
| M09 | [Microsoft Windows event 4625](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625) | Failed logon events. A single event alone does not prove an attack; the benign circumstances here are invented. |
| M08, M10, M11 | Original fictional operational examples | Approved patching, a verified reset, and an expected backup exclusion. These are scenario assumptions, not universal rules for closing alerts. |

The account directory and change records inside the notebook are small fictional, read-only data sets. An approval is matched by record status, asset, event type, account, and time. Merely saying "approved" in an alert does not make the lookup succeed. These records are not live HR or change-management integrations.

## Course and code references

- [Course 06_LangGraph folder](https://github.com/li2cc/IT7075-Applied-AI-for-Cybersecurity/tree/main/06_LangGraph). The first eight parts retain the starter exercise and its supplied twelve practice alerts. The five TODOs are completed; Part 9 contains this project's new scenarios and graph.
- [LangGraph Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api): state, node updates, graph construction, and conditional edges.
- [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence): checkpoints and thread IDs. This project uses an in-memory saver; restarting the kernel clears it.

The practice lookup's CVE-2026-0001 string comes from the course's mock dictionary. It is a teaching placeholder, not verified threat intelligence. The custom project does not rely on it.

Sources checked November 2, 2026.
