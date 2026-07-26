---
title: ActivityUIDismissalPolicy
framework: ActivityKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activityuidismissalpolicy
source_url: 'https://developer.apple.com/documentation/activitykit/activityuidismissalpolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activityuidismissalpolicy.json'
content_hash: 'sha256:d7e715f705243842'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [ActivityKit](../activitykit.md)

# ActivityUIDismissalPolicy

<sub>Structure</sub>

The structure that describes when the system should remove a Live Activity that ended.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct ActivityUIDismissalPolicy
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Dismissing a Live Activity

- [default](activityuidismissalpolicy/default.md) — The system’s default dismissal policy for the Live Activity.
- [immediate](activityuidismissalpolicy/immediate.md) — The system immediately removes the Live Activity that ended.
- [after(_:)](<activityuidismissalpolicy/after(__).md>) — The system removes the Live Activity that ended at the specified time within a four-hour window.

## See Also

### Ending a Live Activity

- [end(_:dismissalPolicy:)](<activity/end(__dismissalpolicy_).md>) — Ends an active Live Activity.
- [end(_:dismissalPolicy:timestamp:)](<activity/end(__dismissalpolicy_timestamp_).md>) — Ends an active Live Activity.
