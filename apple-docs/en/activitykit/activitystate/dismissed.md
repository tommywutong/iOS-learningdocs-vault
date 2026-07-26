---
title: ActivityState.dismissed
framework: ActivityKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activitystate/dismissed
source_url: 'https://developer.apple.com/documentation/activitykit/activitystate/dismissed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activitystate/dismissed.json'
content_hash: 'sha256:73b76ee42bdefe87'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [ActivityState](../activitystate.md)

# ActivityState.dismissed

<sub>Case</sub>

The Live Activity ended and is no longer visible because a person or the system removed it.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
case dismissed
```

## See Also

### Live Activity states

- [ActivityState.active](active.md) — The Live Activity is active, visible, and can receive content updates.
- [ActivityState.pending](pending.md) — The Live Activity is scheduled to start at a specified date but hasn’t started yet.
- [ActivityState.stale](stale.md) — The Live Activity content is out of date and needs an update.
- [ActivityState.ended](ended.md) — The Live Activity is visible, but a person, the app, or the system ended it, and it won’t update its content anymore.
