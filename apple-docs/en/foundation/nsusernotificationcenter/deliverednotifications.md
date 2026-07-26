---
title: deliveredNotifications
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.8+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsusernotificationcenter/deliverednotifications
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotificationcenter/deliverednotifications'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotificationcenter/deliverednotifications.json'
content_hash: 'sha256:5297606993a52b43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotificationCenter](../nsusernotificationcenter.md)

# deliveredNotifications

<sub>Instance Property</sub>

An array of all user notifications delivered to the notification center.

> [!warning] Deprecated
> All NSUserNotifications API should be replaced with UserNotifications.frameworks API

<sub>macOS</sub>

```swift
var deliveredNotifications: [NSUserNotification] { get }
```

## Discussion

The number of notifications the user actually sees in the user interface may be less than the size of this array.

Note that these may or may not have been actually presented to the user. See the [presented](../nsusernotification/ispresented.md) property in the [NSUserNotification](../nsusernotification.md) class.

> [!note] Note
> A scheduled user notification that specifies a [deliveryRepeatInterval](../nsusernotification/deliveryrepeatinterval.md) remains in the [scheduledNotifications](schedulednotifications.md) list, even though it has been delivered.  The item that goes into the `deliveredNotifications` list is a copy of the user notification item.

## See Also

### Managing the Delivered Notifications

- [- deliverNotification:](<deliver(__).md>) — Deliver the specified user notification. _(deprecated)_
- [- removeDeliveredNotification:](<removedeliverednotification(__).md>) — Remove a delivered user notification from the user notification center. _(deprecated)_
- [- removeAllDeliveredNotifications](<removealldeliverednotifications().md>) — Remove all delivered user notifications from the user notification center. _(deprecated)_
