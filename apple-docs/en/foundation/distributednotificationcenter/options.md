---
title: DistributedNotificationCenter.Options
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/distributednotificationcenter/options
source_url: 'https://developer.apple.com/documentation/foundation/distributednotificationcenter/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/distributednotificationcenter/options.json'
content_hash: 'sha256:9fe62b1663d254ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DistributedNotificationCenter](../distributednotificationcenter.md)

# DistributedNotificationCenter.Options

<sub>Structure</sub>

These constants specify the behavior of notifications posted using the [- postNotificationName:object:userInfo:options:](<postnotificationname(__object_userinfo_options_).md>) method.

<sub>Mac Catalyst, macOS</sub>

```swift
struct Options
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSNotificationDeliverImmediately](../nsnotificationdeliverimmediately.md) — When set, the notification is delivered immediately to all observers, regardless of their suspension behavior or suspension state. When not set, allows the normal suspension behavior of notification observers to take place.
- [NSDistributedNotificationDeliverImmediately](options/deliverimmediately.md) — When set, the notification is delivered immediately to all observers, regardless of their suspension behavior or suspension state.
- [NSNotificationPostToAllSessions](../nsnotificationposttoallsessions.md) — When set, the notification is posted to all sessions. When not set, the notification is sent only to applications within the same login session as the posting task.
- [NSDistributedNotificationPostToAllSessions](options/posttoallsessions.md) — When set, the notification is posted to all sessions. When not set, the notification is sent only to applications within the same login session as the posting task.

### Initializers

- [init(rawValue:)](<options/init(rawvalue_).md>)

## See Also

### Constants

- [CenterType](centertype.md) — This constant specifies the notification center type.
- [SuspensionBehavior](suspensionbehavior.md) — These constants specify the types of notification delivery suspension behaviors.
