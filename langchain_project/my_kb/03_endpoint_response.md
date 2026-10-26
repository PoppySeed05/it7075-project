# Harbor SOC: endpoint alert triage

This is a fictional training note for reviewing an endpoint detection alert. Start with the device name, logged-in account, alert time, and detection description. Confirm that the alert belongs to the device listed in the ticket. Check the sensor's last-seen time because a stale console view may not reflect the device's current condition.

## Understand the activity
Review the process tree, including the parent process and command line. Compare the executable path, file signature, and hash with the user's reported activity. Record relevant network destinations and persistence observations. A reputation result is one clue, not a complete verdict. Known administration tools can be abused, and an unfamiliar hash can belong to a harmless new program.

## Isolate with authorization
Network isolation should preserve the endpoint management channel. This lets the authorized responder continue collecting evidence while limiting normal network communication. Obtain the incident lead's approval according to the case procedure and record the reason for isolation. Verify the isolation result in the console. If the tool reports an error or the device is offline, record that limitation instead of assuming the action succeeded.

## Preserve useful evidence
Do not restart or wipe the device simply to make the alert disappear. Those actions can remove useful volatile information and change the evidence available to the responder. Record the alert identifier, important command lines, observed file paths, and action timestamps. Follow the approved evidence process for any collected files. Never upload customer documents or credentials to a public scanning service during triage.

## Coordinate recovery
The incident lead decides when containment can be lifted. Confirm that the assigned investigation and remediation steps are complete, that the device has checked in, and that the user understands any remaining restrictions. Record the approval and time of release. If another team owns reimaging or application restoration, include a named owner and a pending action in the handoff.
