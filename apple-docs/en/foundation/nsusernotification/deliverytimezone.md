---
title: deliveryTimeZone
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.8+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsusernotification/deliverytimezone
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotification/deliverytimezone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotification/deliverytimezone.json'
content_hash: 'sha256:65f06956bb0fc02c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotification](../nsusernotification.md)

# deliveryTimeZone

<sub>Instance Property</sub>

Specify the time zone to interpret the delivery date in.

> [!warning] Deprecated
> All NSUserNotifications API should be replaced with UserNotifications.frameworks API

<sub>macOS</sub>

```swift
var deliveryTimeZone: TimeZone? { get set }
```

## Discussion

If this value is `nil` and the user switches time zones, the notification center will adjust the time of presentation to account for the time zone change.

If a notification should be delivered at a time in a specific time zone (regardless of whether the user switches time zones), set this value to the specific time zone, for example the current time zone.

## See Also

### Delivery Timing

- [deliveryDate](deliverydate.md) — Specifies when the notification should be delivered. _(deprecated)_
- [actualDeliveryDate](actualdeliverydate.md) — The date this notification was actually delivered. _(deprecated)_
- [deliveryRepeatInterval](deliveryrepeatinterval.md) — Specifies the date components that control how often a user notification is repeated. _(deprecated)_
