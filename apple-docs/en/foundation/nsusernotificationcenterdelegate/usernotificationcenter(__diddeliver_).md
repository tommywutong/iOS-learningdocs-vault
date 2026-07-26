---
title: 'userNotificationCenter(_:didDeliver:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.8+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsusernotificationcenterdelegate/usernotificationcenter(_:diddeliver:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotificationcenterdelegate/usernotificationcenter(_:diddeliver:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotificationcenterdelegate/usernotificationcenter%28_%3Adiddeliver%3A%29.json'
content_hash: 'sha256:53702cf74684853f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotificationCenterDelegate](../nsusernotificationcenterdelegate.md)

# userNotificationCenter(_:didDeliver:)

<sub>Instance Method</sub>

Sent to the delegate when a notification delivery date has arrived.

> [!warning] Deprecated
> All NSUserNotifications API should be replaced with UserNotifications.frameworks API

<sub>macOS</sub>

```swift
optional func userNotificationCenter(_ center: NSUserNotificationCenter, didDeliver notification: NSUserNotification)
```

## Parameters

- `center` — The user notification center.

- `notification` — The user notification object.

## Discussion

This method is always called, regardless of your application state and even if you deliver the user notification yourself using [- deliverNotification:](<../nsusernotificationcenter/deliver(__).md>).

This delegate method is invoked before the [- userNotificationCenter:shouldPresentNotification:](<usernotificationcenter(__shouldpresent_).md>) delegate method.

## See Also

### User Notification Delivery Information

- [- userNotificationCenter:didActivateNotification:](<usernotificationcenter(__didactivate_).md>) — Sent to the delegate when a user clicks on a user notification presented by the user notification center. _(deprecated)_
