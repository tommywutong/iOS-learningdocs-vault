---
title: DistributedNotificationCenter.SuspensionBehavior.coalesce
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/distributednotificationcenter/suspensionbehavior/coalesce
source_url: 'https://developer.apple.com/documentation/foundation/distributednotificationcenter/suspensionbehavior/coalesce'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/distributednotificationcenter/suspensionbehavior/coalesce.json'
content_hash: 'sha256:6982f7125bf22064'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [DistributedNotificationCenter](../../distributednotificationcenter.md) · [SuspensionBehavior](../suspensionbehavior.md)

# DistributedNotificationCenter.SuspensionBehavior.coalesce

<sub>Case</sub>

The server only queues the last notification of the specified name and object; earlier notifications are dropped. In cover methods for which suspension behavior is not an explicit argument, `NSNotificationSuspensionBehaviorCoalesce` is the default.

<sub>Mac Catalyst, macOS</sub>

```swift
case coalesce
```

## See Also

### Constants

- [NSNotificationSuspensionBehaviorDrop](drop.md) — The server doesn’t queue any notifications with this name and object until the notification center resumes notification delivery.
- [NSNotificationSuspensionBehaviorHold](hold.md) — The server holds all matching notifications until the queue has been filled (queue size determined by the server), at which point the server may flush queued notifications.
- [NSNotificationSuspensionBehaviorDeliverImmediately](deliverimmediately.md)
