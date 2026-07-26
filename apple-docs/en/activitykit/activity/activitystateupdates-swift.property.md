---
title: activityStateUpdates
framework: ActivityKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activity/activitystateupdates-swift.property
source_url: 'https://developer.apple.com/documentation/activitykit/activity/activitystateupdates-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/activitystateupdates-swift.property.json'
content_hash: 'sha256:4af02bc8a625ba1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [Activity](../activity.md)

# activityStateUpdates

<sub>Instance Property</sub>

An asynchronous sequence you use to observe activity state changes.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var activityStateUpdates: Activity<Attributes>.ActivityStateUpdates { get }
```

## See Also

### Observing the Live Activity life cycle

- [activityState](activitystate.md) — The current state of a Live Activity in its life cycle.
- [ActivityState](../activitystate.md) — The enum that describes the state of a Live Activity in its life cycle.
- [ActivityStateUpdates](activitystateupdates-swift.struct.md) — A structure that offers functionality to observe state changes of a Live Activity.
