---
title: immediate
framework: ActivityKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activityuidismissalpolicy/immediate
source_url: 'https://developer.apple.com/documentation/activitykit/activityuidismissalpolicy/immediate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activityuidismissalpolicy/immediate.json'
content_hash: 'sha256:78d33861451709f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [ActivityUIDismissalPolicy](../activityuidismissalpolicy.md)

# immediate

<sub>Type Property</sub>

The system immediately removes the Live Activity that ended.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static let immediate: ActivityUIDismissalPolicy
```

## Discussion

With the `immediate` dismissal policy, the system immediately removes the ended Live Activity and the [ActivityState](../activitystate.md) changes to [ActivityState.dismissed](../activitystate/dismissed.md).

## See Also

### Dismissing a Live Activity

- [default](default.md) — The system’s default dismissal policy for the Live Activity.
- [after(_:)](<after(__).md>) — The system removes the Live Activity that ended at the specified time within a four-hour window.
