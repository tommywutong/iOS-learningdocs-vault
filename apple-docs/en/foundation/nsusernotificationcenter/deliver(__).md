---
title: 'deliver(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.8+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsusernotificationcenter/deliver(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotificationcenter/deliver(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotificationcenter/deliver%28_%3A%29.json'
content_hash: 'sha256:a868bd8b36735efe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotificationCenter](../nsusernotificationcenter.md)

# deliver(_:)

<sub>Instance Method</sub>

Deliver the specified user notification.

> [!warning] Deprecated
> All NSUserNotifications API should be replaced with UserNotifications.frameworks API

<sub>macOS</sub>

```swift
func deliver(_ notification: NSUserNotification)
```

## Parameters

- `notification` — The user notification.

## Discussion

The notification will be presented to the user (subject to the user’s preferences). The [presented](../nsusernotification/ispresented.md) property of the [NSUserNotification](../nsusernotification.md) object will always be set to [true](../../swift/true.md) if a notification is delivered using this method.

## See Also

### Related Documentation

- [- removeScheduledNotification:](<removeschedulednotification(__).md>) — Removes the specified user notification for the scheduled notifications. _(deprecated)_

### Managing the Delivered Notifications

- [deliveredNotifications](deliverednotifications.md) — An array of all user notifications delivered to the notification center. _(deprecated)_
- [- removeDeliveredNotification:](<removedeliverednotification(__).md>) — Remove a delivered user notification from the user notification center. _(deprecated)_
- [- removeAllDeliveredNotifications](<removealldeliverednotifications().md>) — Remove all delivered user notifications from the user notification center. _(deprecated)_
