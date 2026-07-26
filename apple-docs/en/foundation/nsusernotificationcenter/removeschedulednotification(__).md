---
title: 'removeScheduledNotification(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.8+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsusernotificationcenter/removeschedulednotification(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotificationcenter/removeschedulednotification(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotificationcenter/removeschedulednotification%28_%3A%29.json'
content_hash: 'sha256:1a9d2a2af452a364'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotificationCenter](../nsusernotificationcenter.md)

# removeScheduledNotification(_:)

<sub>Instance Method</sub>

Removes the specified user notification for the scheduled notifications.

> [!warning] Deprecated
> All NSUserNotifications API should be replaced with UserNotifications.frameworks API

<sub>macOS</sub>

```swift
func removeScheduledNotification(_ notification: NSUserNotification)
```

## Parameters

- `notification` — The user notification.

## Discussion

If the user notification’s [deliveryDate](../nsusernotification/deliverydate.md) occurs before the cancellation finishes, the notification may still be delivered.

If the notification is not in the scheduled list, nothing happens.

## See Also

### Managing the Scheduled Notification Queue

- [- scheduleNotification:](<schedulenotification(__).md>) — Schedules the specified user notification. _(deprecated)_
- [scheduledNotifications](schedulednotifications.md) — Specifies an array of scheduled user notifications that have not yet been delivered. _(deprecated)_
