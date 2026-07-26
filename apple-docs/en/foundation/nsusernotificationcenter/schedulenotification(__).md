---
title: 'scheduleNotification(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.8+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsusernotificationcenter/schedulenotification(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotificationcenter/schedulenotification(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotificationcenter/schedulenotification%28_%3A%29.json'
content_hash: 'sha256:5e9a234c2ff7e48d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotificationCenter](../nsusernotificationcenter.md)

# scheduleNotification(_:)

<sub>Instance Method</sub>

Schedules the specified user notification.

> [!warning] Deprecated
> All NSUserNotifications API should be replaced with UserNotifications.frameworks API

<sub>macOS</sub>

```swift
func scheduleNotification(_ notification: NSUserNotification)
```

## Parameters

- `notification` — The user notification.

## Discussion

Scheduled notifications are added to the end of the notification queue.

## See Also

### Related Documentation

- [- deliverNotification:](<deliver(__).md>) — Deliver the specified user notification. _(deprecated)_

### Managing the Scheduled Notification Queue

- [scheduledNotifications](schedulednotifications.md) — Specifies an array of scheduled user notifications that have not yet been delivered. _(deprecated)_
- [- removeScheduledNotification:](<removeschedulednotification(__).md>) — Removes the specified user notification for the scheduled notifications. _(deprecated)_
