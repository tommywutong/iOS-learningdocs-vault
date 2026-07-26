---
title: CFNotificationSuspensionBehavior.coalesce
framework: Core Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfnotificationsuspensionbehavior/coalesce
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnotificationsuspensionbehavior/coalesce'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnotificationsuspensionbehavior/coalesce.json'
content_hash: 'sha256:23420fab812a6f76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFNotificationSuspensionBehavior](../cfnotificationsuspensionbehavior.md)

# CFNotificationSuspensionBehavior.coalesce

<sub>Case</sub>

The server will only queue the last notification of the specified name and object; earlier notifications are dropped.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case coalesce
```

## See Also

### Constants

- [CFNotificationSuspensionBehaviorDrop](drop.md) — The server will not queue any notifications of the specified name and object while the receiving application is in the background.
- [CFNotificationSuspensionBehaviorHold](hold.md) — The server will hold all matching notifications until the queue has been filled (queue size determined by the server) at which point the server may flush queued notifications.
- [CFNotificationSuspensionBehaviorDeliverImmediately](deliverimmediately.md) — The server will deliver notifications of the specified name and object whether or not the application is in the background. When a notification with this suspension behavior is matched, it has the effect of first flushing any queued notifications.
