---
title: DistributedNotificationCenter.SuspensionBehavior.hold
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/distributednotificationcenter/suspensionbehavior/hold
source_url: 'https://developer.apple.com/documentation/foundation/distributednotificationcenter/suspensionbehavior/hold'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/distributednotificationcenter/suspensionbehavior/hold.json'
content_hash: 'sha256:3df73e2c4568f01e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [DistributedNotificationCenter](../../distributednotificationcenter.md) · [SuspensionBehavior](../suspensionbehavior.md)

# DistributedNotificationCenter.SuspensionBehavior.hold

<sub>Case</sub>

The server holds all matching notifications until the queue has been filled (queue size determined by the server), at which point the server may flush queued notifications.

<sub>Mac Catalyst, macOS</sub>

```swift
case hold
```

## See Also

### Constants

- [NSNotificationSuspensionBehaviorDrop](drop.md) — The server doesn’t queue any notifications with this name and object until the notification center resumes notification delivery.
- [NSNotificationSuspensionBehaviorCoalesce](coalesce.md) — The server only queues the last notification of the specified name and object; earlier notifications are dropped. In cover methods for which suspension behavior is not an explicit argument, `NSNotificationSuspensionBehaviorCoalesce` is the default.
- [NSNotificationSuspensionBehaviorDeliverImmediately](deliverimmediately.md)
