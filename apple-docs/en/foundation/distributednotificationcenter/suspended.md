---
title: suspended
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/distributednotificationcenter/suspended
source_url: 'https://developer.apple.com/documentation/foundation/distributednotificationcenter/suspended'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/distributednotificationcenter/suspended.json'
content_hash: 'sha256:ba828de250ba0930'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DistributedNotificationCenter](../distributednotificationcenter.md)

# suspended

<sub>Instance Property</sub>

Suspends or resumes notification delivery.

<sub>Mac Catalyst, macOS</sub>

```swift
var suspended: Bool { get set }
```

## Parameters

- `suspended` — [true](../../swift/true.md) suspends notification delivery, [false](../../swift/false.md) resumes it.

## Discussion

See [SuspensionBehavior](suspensionbehavior.md) for details on how the receiver delivers notifications to their observers when normal notification delivery is suspended.

The [NSApplication](../../appkit/nsapplication.md) class automatically suspends distributed notification delivery when the application is not active. Applications based on the Application Kit framework should let AppKit manage the suspension of notification delivery. Foundation-only programs may have occasional need to use this method.

## See Also

### Related Documentation

- [- addObserver:selector:name:object:suspensionBehavior:](<addobserver(__selector_name_object_suspensionbehavior_).md>) — Adds an entry to the receiver’s dispatch table with a specific observer and suspended-notifications behavior, and optional notification name and sender.
- [- postNotificationName:object:userInfo:deliverImmediately:](<postnotificationname(__object_userinfo_deliverimmediately_).md>) — Creates a notification with information and an immediate-delivery specifier, and posts it to the receiver.
