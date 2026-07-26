---
title: default
framework: ActivityKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activityuidismissalpolicy/default
source_url: 'https://developer.apple.com/documentation/activitykit/activityuidismissalpolicy/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activityuidismissalpolicy/default.json'
content_hash: 'sha256:d15c3fefefe663d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [ActivityUIDismissalPolicy](../activityuidismissalpolicy.md)

# default

<sub>Type Property</sub>

The system’s default dismissal policy for the Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static let `default`: ActivityUIDismissalPolicy
```

## Discussion

With the default dismissal policy, the system keeps a Live Activity that ended on the Lock Screen for up to four hours after it ends or a person removes it. The [ActivityState](../activitystate.md) doesn’t change to [ActivityState.dismissed](../activitystate/dismissed.md) until a person or the system removes the Live Activity user interface.

## See Also

### Dismissing a Live Activity

- [immediate](immediate.md) — The system immediately removes the Live Activity that ended.
- [after(_:)](<after(__).md>) — The system removes the Live Activity that ended at the specified time within a four-hour window.
