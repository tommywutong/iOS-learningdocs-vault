---
title: scheduledNotifications
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.8+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsusernotificationcenter/schedulednotifications
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotificationcenter/schedulednotifications'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotificationcenter/schedulednotifications.json'
content_hash: 'sha256:3840f40a70dfa41e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotificationCenter](../nsusernotificationcenter.md)

# scheduledNotifications

<sub>Instance Property</sub>

Specifies an array of scheduled user notifications that have not yet been delivered.

> [!warning] Deprecated
> All NSUserNotifications API should be replaced with UserNotifications.frameworks API

<sub>macOS</sub>

```swift
var scheduledNotifications: [NSUserNotification] { get set }
```

## Discussion

Newly scheduled notifications are added to the end of the array. You may also bulk-schedule notifications by setting this array. Bulk setting new scheduled notifications unschedules existing notifications.

> [!note] Note
> The scheduled user notification could be changing to a delivered notification at the time you are calling this method. and if that case the user notification will still be delivered.

## See Also

### Managing the Scheduled Notification Queue

- [- scheduleNotification:](<schedulenotification(__).md>) — Schedules the specified user notification. _(deprecated)_
- [- removeScheduledNotification:](<removeschedulednotification(__).md>) — Removes the specified user notification for the scheduled notifications. _(deprecated)_
