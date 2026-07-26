---
title: delegate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.8+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsusernotificationcenter/delegate
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotificationcenter/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotificationcenter/delegate.json'
content_hash: 'sha256:b8944b80788c2000'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotificationCenter](../nsusernotificationcenter.md)

# delegate

<sub>Instance Property</sub>

Specifies the notification center delegate.

> [!warning] Deprecated
> All NSUserNotifications API should be replaced with UserNotifications.frameworks API

<sub>macOS</sub>

```swift
unowned(unsafe) var delegate: (any NSUserNotificationCenterDelegate)? { get set }
```

## Discussion

The delegate must conform to the [NSUserNotificationCenterDelegate](../nsusernotificationcenterdelegate.md) protocol.
