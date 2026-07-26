---
title: 'after(_:)'
framework: ActivityKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/activitykit/activityuidismissalpolicy/after(_:)'
source_url: 'https://developer.apple.com/documentation/activitykit/activityuidismissalpolicy/after(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activityuidismissalpolicy/after%28_%3A%29.json'
content_hash: 'sha256:ae7c473bc71ed58b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [ActivityUIDismissalPolicy](../activityuidismissalpolicy.md)

# after(_:)

<sub>Type Method</sub>

The system removes the Live Activity that ended at the specified time within a four-hour window.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static func after(_ date: Date) -> ActivityUIDismissalPolicy
```

## Parameters

- `date` — A date within a four-hour window from the moment the Live Activity ends.

## Discussion

Provide a date to tell the system when it should remove a Live Activity that ended. While you can provide any date, the system removes a Live Activity that ended after the specified date or after four hours from the moment the Live Activity ended — whichever comes first. When the system removes the Live Activity,  the [ActivityState](../activitystate.md) changes to [ActivityState.dismissed](../activitystate/dismissed.md).

## See Also

### Dismissing a Live Activity

- [default](default.md) — The system’s default dismissal policy for the Live Activity.
- [immediate](immediate.md) — The system immediately removes the Live Activity that ended.
