---
title: ActivityState.pending
framework: ActivityKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activitystate/pending
source_url: 'https://developer.apple.com/documentation/activitykit/activitystate/pending'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activitystate/pending.json'
content_hash: 'sha256:90889847eb440a55'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [ActivityState](../activitystate.md)

# ActivityState.pending

<sub>Case</sub>

The Live Activity is scheduled to start at a specified date but hasn’t started yet.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
case pending
```

## See Also

### Live Activity states

- [ActivityState.active](active.md) — The Live Activity is active, visible, and can receive content updates.
- [ActivityState.dismissed](dismissed.md) — The Live Activity ended and is no longer visible because a person or the system removed it.
- [ActivityState.stale](stale.md) — The Live Activity content is out of date and needs an update.
- [ActivityState.ended](ended.md) — The Live Activity is visible, but a person, the app, or the system ended it, and it won’t update its content anymore.
