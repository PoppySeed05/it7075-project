# Harbor SOC: account compromise review

This fictional procedure covers initial review of a potentially compromised account. The analyst first checks the report against sign-in records and contacts the user through a previously known channel. A message from the suspicious session is not sufficient identity verification. Separate what the user confirms from what the logs suggest.

## Contain an active session
For a confirmed compromise, revoke active sessions after resetting the password. Follow the incident lead's authorization process for disabling access when activity is still ongoing. A password reset by itself may leave an existing session usable. Record the start and completion times of each containment action in the case. Do not claim that the account is safe just because one control reports success.

## Review account changes
Check recent MFA device registrations, recovery contact changes, and consent grants for unfamiliar entries. Record the identifier and creation time of any suspicious item before asking the authorized administrator to remove it. Compare the changes to the user's normal activity. A new phone or a planned device migration can explain a legitimate change, so check context instead of assuming every new entry is hostile.

## Review the mailbox
Look for forwarding rules that send mail to an unfamiliar external address. Also inspect rules that delete messages, mark messages as read, or move security notifications into an unusual folder. Record the rule name, action, target, and creation time if available. Preserve the relevant details before an authorized administrator removes a malicious rule. Check sent mail for messages the user does not recognize and record the affected recipients for the incident lead.

## Verify recovery
Ask the user to sign in through the normal company portal after recovery is complete. Verify that approved MFA methods work and that the suspicious changes are gone. Continue reviewing new authentication events during the case's follow-up window. Document unexplained activity and keep the case open if required checks have not finished. The analyst should distinguish a failed login from a successful session and should avoid assuming that an IP address identifies a person.
