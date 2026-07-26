---
title: 'removeDeliveredNotification(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.8+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsusernotificationcenter/removedeliverednotification(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotificationcenter/removedeliverednotification(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotificationcenter/removedeliverednotification%28_%3A%29.json'
content_hash: 'sha256:dae4e8c5d717db63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotificationCenter](../nsusernotificationcenter.md)

# removeDeliveredNotification(_:)

<sub>Instance Method</sub>

Remove a delivered user notification from the user notification center.

> [!warning] Deprecated
> All NSUserNotifications API should be replaced with UserNotifications.frameworks API

<sub>macOS</sub>

```swift
func removeDeliveredNotification(_ notification: NSUserNotification)
```

## Parameters

- `notification` — The user notification.

## Discussion

If the user notification is not in [deliveredNotifications](deliverednotifications.md), nothing happens.

## See Also

### Managing the Delivered Notifications

- [- deliverNotification:](<deliver(__).md>) — Deliver the specified user notification. _(deprecated)_
- [deliveredNotifications](deliverednotifications.md) — An array of all user notifications delivered to the notification center. _(deprecated)_
- [- removeAllDeliveredNotifications](<removealldeliverednotifications().md>) — Remove all delivered user notifications from the user notification center. _(deprecated)_
