---
title: userInfo
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.8+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsusernotification/userinfo
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotification/userinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotification/userinfo.json'
content_hash: 'sha256:4e8a3e9002d5451d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotification](../nsusernotification.md)

# userInfo

<sub>Instance Property</sub>

Application-specific user info that can be attached to the notification.

> [!warning] Deprecated
> All NSUserNotifications API should be replaced with UserNotifications.frameworks API

<sub>macOS</sub>

```swift
var userInfo: [String : Any]? { get set }
```

## Discussion

All items must be property list types or an exception is thrown.

The `userInfo` content must be of reasonable serialized size (less than 1KB) or an exception is thrown.
