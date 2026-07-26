---
title: NSNotificationPostToAllSessions
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotificationposttoallsessions
source_url: 'https://developer.apple.com/documentation/foundation/nsnotificationposttoallsessions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotificationposttoallsessions.json'
content_hash: 'sha256:ed9f5b2b75d87fc9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSNotificationPostToAllSessions

<sub>Global Variable</sub>

When set, the notification is posted to all sessions. When not set, the notification is sent only to applications within the same login session as the posting task.

<sub>Mac Catalyst, macOS</sub>

```swift
var NSNotificationPostToAllSessions: DistributedNotificationCenter.Options { get }
```

## See Also

### Constants

- [NSNotificationDeliverImmediately](nsnotificationdeliverimmediately.md) — When set, the notification is delivered immediately to all observers, regardless of their suspension behavior or suspension state. When not set, allows the normal suspension behavior of notification observers to take place.
- [NSDistributedNotificationDeliverImmediately](distributednotificationcenter/options/deliverimmediately.md) — When set, the notification is delivered immediately to all observers, regardless of their suspension behavior or suspension state.
- [NSDistributedNotificationPostToAllSessions](distributednotificationcenter/options/posttoallsessions.md) — When set, the notification is posted to all sessions. When not set, the notification is sent only to applications within the same login session as the posting task.
