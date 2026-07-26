---
title: CFNotificationSuspensionBehavior.hold
framework: Core Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfnotificationsuspensionbehavior/hold
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnotificationsuspensionbehavior/hold'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnotificationsuspensionbehavior/hold.json'
content_hash: 'sha256:c56b28ede8f3389c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFNotificationSuspensionBehavior](../cfnotificationsuspensionbehavior.md)

# CFNotificationSuspensionBehavior.hold

<sub>Case</sub>

The server will hold all matching notifications until the queue has been filled (queue size determined by the server) at which point the server may flush queued notifications.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case hold
```

## See Also

### Constants

- [CFNotificationSuspensionBehaviorDrop](drop.md) — The server will not queue any notifications of the specified name and object while the receiving application is in the background.
- [CFNotificationSuspensionBehaviorCoalesce](coalesce.md) — The server will only queue the last notification of the specified name and object; earlier notifications are dropped.
- [CFNotificationSuspensionBehaviorDeliverImmediately](deliverimmediately.md) — The server will deliver notifications of the specified name and object whether or not the application is in the background. When a notification with this suspension behavior is matched, it has the effect of first flushing any queued notifications.
