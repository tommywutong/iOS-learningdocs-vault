---
title: onSender
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationqueue/notificationcoalescing/onsender
source_url: 'https://developer.apple.com/documentation/foundation/notificationqueue/notificationcoalescing/onsender'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationqueue/notificationcoalescing/onsender.json'
content_hash: 'sha256:6f6f4c838fc3eb0e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationQueue](../../notificationqueue.md) · [NotificationCoalescing](../notificationcoalescing.md)

# onSender

<sub>Type Property</sub>

Coalesce notifications with the same object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var onSender: NotificationQueue.NotificationCoalescing { get }
```

## See Also

### Constants

- [NSNotificationNoCoalescing](none.md) — Do not coalesce notifications in the queue.
- [NSNotificationCoalescingOnName](onname.md) — Coalesce notifications with the same name.
