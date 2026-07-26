---
title: ActivityState
framework: ActivityKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activitystate
source_url: 'https://developer.apple.com/documentation/activitykit/activitystate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activitystate.json'
content_hash: 'sha256:316df420d930a5ea'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [ActivityKit](../activitykit.md)

# ActivityState

<sub>Enumeration</sub>

The enum that describes the state of a Live Activity in its life cycle.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
enum ActivityState
```

## Relationships

- **Conforms To**: [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Live Activity states

- [ActivityState.active](activitystate/active.md) — The Live Activity is active, visible, and can receive content updates.
- [ActivityState.dismissed](activitystate/dismissed.md) — The Live Activity ended and is no longer visible because a person or the system removed it.
- [ActivityState.pending](activitystate/pending.md) — The Live Activity is scheduled to start at a specified date but hasn’t started yet.
- [ActivityState.stale](activitystate/stale.md) — The Live Activity content is out of date and needs an update.
- [ActivityState.ended](activitystate/ended.md) — The Live Activity is visible, but a person, the app, or the system ended it, and it won’t update its content anymore.

## See Also

### Observing the Live Activity life cycle

- [activityState](activity/activitystate.md) — The current state of a Live Activity in its life cycle.
- [activityStateUpdates](activity/activitystateupdates-swift.property.md) — An asynchronous sequence you use to observe activity state changes.
- [ActivityStateUpdates](activity/activitystateupdates-swift.struct.md) — A structure that offers functionality to observe state changes of a Live Activity.
