---
title: postToAllSessions
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/distributednotificationcenter/options/posttoallsessions
source_url: 'https://developer.apple.com/documentation/foundation/distributednotificationcenter/options/posttoallsessions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/distributednotificationcenter/options/posttoallsessions.json'
content_hash: 'sha256:74d5b61d2b581ed0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [DistributedNotificationCenter](../../distributednotificationcenter.md) · [Options](../options.md)

# postToAllSessions

<sub>Type Property</sub>

When set, the notification is posted to all sessions. When not set, the notification is sent only to applications within the same login session as the posting task.

<sub>Mac Catalyst, macOS</sub>

```swift
static var postToAllSessions: DistributedNotificationCenter.Options { get }
```

## See Also

### Constants

- [NSNotificationDeliverImmediately](../../nsnotificationdeliverimmediately.md) — When set, the notification is delivered immediately to all observers, regardless of their suspension behavior or suspension state. When not set, allows the normal suspension behavior of notification observers to take place.
- [NSDistributedNotificationDeliverImmediately](deliverimmediately.md) — When set, the notification is delivered immediately to all observers, regardless of their suspension behavior or suspension state.
- [NSNotificationPostToAllSessions](../../nsnotificationposttoallsessions.md) — When set, the notification is posted to all sessions. When not set, the notification is sent only to applications within the same login session as the posting task.
