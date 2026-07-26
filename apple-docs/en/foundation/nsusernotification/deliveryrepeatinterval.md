---
title: deliveryRepeatInterval
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.8+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsusernotification/deliveryrepeatinterval
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotification/deliveryrepeatinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotification/deliveryrepeatinterval.json'
content_hash: 'sha256:c41e1401a3add9a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotification](../nsusernotification.md)

# deliveryRepeatInterval

<sub>Instance Property</sub>

Specifies the date components that control how often a user notification is repeated.

> [!warning] Deprecated
> All NSUserNotifications API should be replaced with UserNotifications.frameworks API

<sub>macOS</sub>

```swift
var deliveryRepeatInterval: DateComponents? { get set }
```

## Discussion

This value may be `nil` if the notification should not repeat.

The date component values are relative to the date the notification was delivered.

If the calendar value of the `deliveryRepeatInterval` is `nil`, the current calendar is used to calculate the repeat interval. For example, if a notification should repeat every hour, set the `hour` property of the `deliveryRepeatInterval` to `1`.

This value is ignored unless the user notification is scheduled with the [NSUserNotificationCenter](../nsusernotificationcenter.md) object.

## See Also

### Delivery Timing

- [deliveryDate](deliverydate.md) — Specifies when the notification should be delivered. _(deprecated)_
- [actualDeliveryDate](actualdeliverydate.md) — The date this notification was actually delivered. _(deprecated)_
- [deliveryTimeZone](deliverytimezone.md) — Specify the time zone to interpret the delivery date in. _(deprecated)_
