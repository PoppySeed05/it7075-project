## Build a readable timeline
Use UTC timestamps in the incident timeline. Record the source's original timezone when converting a log entry, and preserve the original event identifier when available. Note both the event time and the time the analyst performed an action if those differ. Do not invent an exact timestamp when the only information available is a user's approximate recollection. Mark approximate times as estimates.

## Describe the current state
State what triggered the investigation, what systems or accounts are affected, and what containment has actually been confirmed. Link to the restricted evidence location rather than pasting confidential material into a broadly visible note. Mention failed actions, unavailable logs, and incomplete checks. If the team has only a suspicion, label it as a hypothesis and state what observation would support or weaken it.

## Assign the next action
Every handoff must include the next action and its owner. Also record the pending question, expected follow-up time, and the condition that should trigger escalation. For example, the next analyst might need to verify whether a revoked session continues to appear in new authentication events. The example describes a check to perform, not proof that the original containment failed.

## Close with a reason
Before closure, confirm that the assigned checks are finished or that remaining work has a documented owner outside the case. Summarize the evidence for the final classification and note any residual uncertainty. If the user needs a follow-up message, make that an explicit action instead of assuming another shift will send it. Avoid blame and focus on what happened, what was verified, and what remains.
