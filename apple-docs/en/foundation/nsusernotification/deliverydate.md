---
title: deliveryDate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.8+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsusernotification/deliverydate
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotification/deliverydate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotification/deliverydate.json'
content_hash: 'sha256:05c4b5703d2a17a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotification](../nsusernotification.md)

# deliveryDate

<sub>Instance Property</sub>

Specifies when the notification should be delivered.

> [!warning] Deprecated
> All NSUserNotifications API should be replaced with UserNotifications.frameworks API

<sub>macOS</sub>

```swift
var deliveryDate: Date? { get set }
```

## Discussion

The delivery date is specified in an absolute time.

After a notification is delivered, it may be presented to the user.

## See Also

### Delivery Timing

- [actualDeliveryDate](actualdeliverydate.md) — The date this notification was actually delivered. _(deprecated)_
- [deliveryRepeatInterval](deliveryrepeatinterval.md) — Specifies the date components that control how often a user notification is repeated. _(deprecated)_
- [deliveryTimeZone](deliverytimezone.md) — Specify the time zone to interpret the delivery date in. _(deprecated)_
