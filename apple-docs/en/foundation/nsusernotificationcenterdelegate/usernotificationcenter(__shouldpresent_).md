---
title: 'userNotificationCenter(_:shouldPresent:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.8+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsusernotificationcenterdelegate/usernotificationcenter(_:shouldpresent:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotificationcenterdelegate/usernotificationcenter(_:shouldpresent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotificationcenterdelegate/usernotificationcenter%28_%3Ashouldpresent%3A%29.json'
content_hash: 'sha256:b96c8b150bbd0338'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotificationCenterDelegate](../nsusernotificationcenterdelegate.md)

# userNotificationCenter(_:shouldPresent:)

<sub>Instance Method</sub>

Sent to the delegate when the user notification center has decided not to present your notification.

> [!warning] Deprecated
> All NSUserNotifications API should be replaced with UserNotifications.frameworks API

<sub>macOS</sub>

```swift
optional func userNotificationCenter(_ center: NSUserNotificationCenter, shouldPresent notification: NSUserNotification) -> Bool
```

## Parameters

- `center` — The user notification center.

- `notification` — The user notification object.

## Return Value

[true](../../swift/true.md) if the user notification should be displayed regardless; [false](../../swift/false.md) otherwise.
