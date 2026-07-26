---
title: actualDeliveryDate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.8+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsusernotification/actualdeliverydate
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotification/actualdeliverydate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotification/actualdeliverydate.json'
content_hash: 'sha256:0296966e0aaa7b6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotification](../nsusernotification.md)

# actualDeliveryDate

<sub>Instance Property</sub>

The date this notification was actually delivered.

> [!warning] Deprecated
> All NSUserNotifications API should be replaced with UserNotifications.frameworks API

<sub>macOS</sub>

```swift
var actualDeliveryDate: Date? { get }
```

## Discussion

The notification center will set this value if a notification is put in the scheduled list and the delivery time arrives.

If the notification is delivered directly using the [- deliverNotification:](<../nsusernotificationcenter/deliver(__).md>) method of the [NSUserNotificationCenter](../nsusernotificationcenter.md) class, this value is set to the [deliveryDate](deliverydate.md) value. If the [deliveryDate](deliverydate.md) value `nil`  this value is set to the current date.

This value is used to sort the list of notifications in the user interface.

## See Also

### Delivery Timing

- [deliveryDate](deliverydate.md) — Specifies when the notification should be delivered. _(deprecated)_
- [deliveryRepeatInterval](deliveryrepeatinterval.md) — Specifies the date components that control how often a user notification is repeated. _(deprecated)_
- [deliveryTimeZone](deliverytimezone.md) — Specify the time zone to interpret the delivery date in. _(deprecated)_
