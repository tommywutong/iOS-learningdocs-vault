---
title: DistributedNotificationCenter.SuspensionBehavior
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/distributednotificationcenter/suspensionbehavior
source_url: 'https://developer.apple.com/documentation/foundation/distributednotificationcenter/suspensionbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/distributednotificationcenter/suspensionbehavior.json'
content_hash: 'sha256:79c9a870bcc1647b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DistributedNotificationCenter](../distributednotificationcenter.md)

# DistributedNotificationCenter.SuspensionBehavior

<sub>Enumeration</sub>

These constants specify the types of notification delivery suspension behaviors.

<sub>Mac Catalyst, macOS</sub>

```swift
enum SuspensionBehavior
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSNotificationSuspensionBehaviorDrop](suspensionbehavior/drop.md) — The server doesn’t queue any notifications with this name and object until the notification center resumes notification delivery.
- [NSNotificationSuspensionBehaviorCoalesce](suspensionbehavior/coalesce.md) — The server only queues the last notification of the specified name and object; earlier notifications are dropped. In cover methods for which suspension behavior is not an explicit argument, `NSNotificationSuspensionBehaviorCoalesce` is the default.
- [NSNotificationSuspensionBehaviorHold](suspensionbehavior/hold.md) — The server holds all matching notifications until the queue has been filled (queue size determined by the server), at which point the server may flush queued notifications.
- [NSNotificationSuspensionBehaviorDeliverImmediately](suspensionbehavior/deliverimmediately.md)

### Initializers

- [init(rawValue:)](<suspensionbehavior/init(rawvalue_).md>)

## See Also

### Constants

- [Options](options.md) — These constants specify the behavior of notifications posted using the [- postNotificationName:object:userInfo:options:](<postnotificationname(__object_userinfo_options_).md>) method.
- [CenterType](centertype.md) — This constant specifies the notification center type.
