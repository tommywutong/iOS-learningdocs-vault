---
title: regionTriggersOnce
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilocalnotification/regiontriggersonce
source_url: 'https://developer.apple.com/documentation/uikit/uilocalnotification/regiontriggersonce'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilocalnotification/regiontriggersonce.json'
content_hash: 'sha256:da79974fd5353097'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILocalNotification](../uilocalnotification.md)

# regionTriggersOnce

<sub>Instance Property</sub>

A Boolean value indicating whether crossing a geographic region boundary delivers only one notification.

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
var regionTriggersOnce: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md), the user is notified only upon the first crossing the boundary of the target [region](region.md). After the first crossing, the local notification is unscheduled. When the value of this property is [false](../../swift/false.md), notifications are delivered with each boundary crossing. The default value of this property is [true](../../swift/true.md).

The region object itself defines whether the notification is triggered when the user enters or exits the region.

## See Also

### Scheduling a local notification

- [fireDate](firedate.md) — The date and time when the system should deliver the notification. _(deprecated)_
- [timeZone](timezone.md) — The time zone of the notification’s fire date. _(deprecated)_
- [repeatInterval](repeatinterval.md) — The calendar interval at which to reschedule the notification. _(deprecated)_
- [repeatCalendar](repeatcalendar.md) — The calendar the system should refer to when it reschedules a repeating notification. _(deprecated)_
- [region](region.md) — The geographic region that triggers the notification. _(deprecated)_
