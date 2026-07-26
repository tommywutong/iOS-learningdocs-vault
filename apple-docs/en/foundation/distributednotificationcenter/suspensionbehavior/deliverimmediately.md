---
title: DistributedNotificationCenter.SuspensionBehavior.deliverImmediately
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/distributednotificationcenter/suspensionbehavior/deliverimmediately
source_url: 'https://developer.apple.com/documentation/foundation/distributednotificationcenter/suspensionbehavior/deliverimmediately'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/distributednotificationcenter/suspensionbehavior/deliverimmediately.json'
content_hash: 'sha256:8fc3e9fc9275e43c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [DistributedNotificationCenter](../../distributednotificationcenter.md) · [SuspensionBehavior](../suspensionbehavior.md)

# DistributedNotificationCenter.SuspensionBehavior.deliverImmediately

<sub>Case</sub>

<sub>Mac Catalyst, macOS</sub>

```swift
case deliverImmediately
```

## Discussion

The server delivers notifications matching this registration irrespective of whether [suspended](../suspended.md) with an argument of [true](../../../swift/true.md) has been called. When a notification with this suspension behavior is matched, it has the effect of first flushing any queued notifications. The effect is as if [suspended](../suspended.md) with an argument of [false](../../../swift/false.md) were first called if the application is suspended, followed by the notification in question being delivered, followed by a transition back to the previous suspended or unsuspended state.

## See Also

### Constants

- [NSNotificationSuspensionBehaviorDrop](drop.md) — The server doesn’t queue any notifications with this name and object until the notification center resumes notification delivery.
- [NSNotificationSuspensionBehaviorCoalesce](coalesce.md) — The server only queues the last notification of the specified name and object; earlier notifications are dropped. In cover methods for which suspension behavior is not an explicit argument, `NSNotificationSuspensionBehaviorCoalesce` is the default.
- [NSNotificationSuspensionBehaviorHold](hold.md) — The server holds all matching notifications until the queue has been filled (queue size determined by the server), at which point the server may flush queued notifications.
