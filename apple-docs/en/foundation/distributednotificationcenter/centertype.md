---
title: DistributedNotificationCenter.CenterType
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/distributednotificationcenter/centertype
source_url: 'https://developer.apple.com/documentation/foundation/distributednotificationcenter/centertype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/distributednotificationcenter/centertype.json'
content_hash: 'sha256:ddd85a4bafd7cbac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DistributedNotificationCenter](../distributednotificationcenter.md)

# DistributedNotificationCenter.CenterType

<sub>Structure</sub>

This constant specifies the notification center type.

<sub>Mac Catalyst, macOS</sub>

```swift
struct CenterType
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Type Properties

- [NSLocalNotificationCenterType](centertype/localnotificationcentertype.md) — Distributes notifications to all tasks on the sender’s computer.

### Initializers

- [init(_:)](<centertype/init(__).md>)
- [init(rawValue:)](<centertype/init(rawvalue_).md>)

## See Also

### Constants

- [Options](options.md) — These constants specify the behavior of notifications posted using the [- postNotificationName:object:userInfo:options:](<postnotificationname(__object_userinfo_options_).md>) method.
- [SuspensionBehavior](suspensionbehavior.md) — These constants specify the types of notification delivery suspension behaviors.
