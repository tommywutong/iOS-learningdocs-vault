---
title: DistributedNotificationCenter.SuspensionBehavior.drop
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/distributednotificationcenter/suspensionbehavior/drop
source_url: 'https://developer.apple.com/documentation/foundation/distributednotificationcenter/suspensionbehavior/drop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/distributednotificationcenter/suspensionbehavior/drop.json'
content_hash: 'sha256:39b5e18c02dac154'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [DistributedNotificationCenter](../../distributednotificationcenter.md) · [SuspensionBehavior](../suspensionbehavior.md)

# DistributedNotificationCenter.SuspensionBehavior.drop

<sub>Case</sub>

The server doesn’t queue any notifications with this name and object until the notification center resumes notification delivery.

<sub>Mac Catalyst, macOS</sub>

```swift
case drop
```

## Discussion

To resume notification delivery, set the [suspended](../suspended.md) to [false](../../../swift/false.md).

## See Also

### Constants

- [NSNotificationSuspensionBehaviorCoalesce](coalesce.md) — The server only queues the last notification of the specified name and object; earlier notifications are dropped. In cover methods for which suspension behavior is not an explicit argument, `NSNotificationSuspensionBehaviorCoalesce` is the default.
- [NSNotificationSuspensionBehaviorHold](hold.md) — The server holds all matching notifications until the queue has been filled (queue size determined by the server), at which point the server may flush queued notifications.
- [NSNotificationSuspensionBehaviorDeliverImmediately](deliverimmediately.md)
