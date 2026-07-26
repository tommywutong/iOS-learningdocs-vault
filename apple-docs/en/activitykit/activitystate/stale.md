---
title: ActivityState.stale
framework: ActivityKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.2+, iPadOS 16.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activitystate/stale
source_url: 'https://developer.apple.com/documentation/activitykit/activitystate/stale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activitystate/stale.json'
content_hash: 'sha256:b9980a1d8dbea79f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [ActivityState](../activitystate.md)

# ActivityState.stale

<sub>Case</sub>

The Live Activity content is out of date and needs an update.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
case stale
```

## Discussion

The content of a Live Activity may become out of date before you can update it. For example, a person may be in an area without a network connection, causing the Live Activity to not receive updates. To tell people that they are looking at outdated Live Activity content, you can configure a [staleDate](../activitycontent/staledate.md) for your Live Activity. At the specified date, the [activityState](../activity/activitystate.md) changes to `stale` and you can update the Live Activity to indicate that its content is out of date.

## See Also

### Live Activity states

- [ActivityState.active](active.md) — The Live Activity is active, visible, and can receive content updates.
- [ActivityState.dismissed](dismissed.md) — The Live Activity ended and is no longer visible because a person or the system removed it.
- [ActivityState.pending](pending.md) — The Live Activity is scheduled to start at a specified date but hasn’t started yet.
- [ActivityState.ended](ended.md) — The Live Activity is visible, but a person, the app, or the system ended it, and it won’t update its content anymore.
