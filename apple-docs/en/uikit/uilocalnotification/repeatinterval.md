---
title: repeatInterval
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilocalnotification/repeatinterval
source_url: 'https://developer.apple.com/documentation/uikit/uilocalnotification/repeatinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilocalnotification/repeatinterval.json'
content_hash: 'sha256:71f3aff4001c3539'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILocalNotification](../uilocalnotification.md)

# repeatInterval

<sub>Instance Property</sub>

The calendar interval at which to reschedule the notification.

> [!warning] Deprecated
> For more information, see [UILocalNotification](../uilocalnotification.md).

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
var repeatInterval: NSCalendar.Unit { get set }
```

## Discussion

If you assign a calendar unit such as weekly ([weekOfYear](../../foundation/nscalendar/unit/weekofyear.md)) or yearly ([year](../../foundation/nscalendar/unit/year.md)), the system reschedules the notification for delivery at the specified interval. Note that intervals of less than one minute are not supported. The default value is 0, which means that the system fires the notification once and then discards it.

## See Also

### Scheduling a local notification

- [fireDate](firedate.md) — The date and time when the system should deliver the notification. _(deprecated)_
- [timeZone](timezone.md) — The time zone of the notification’s fire date. _(deprecated)_
- [repeatCalendar](repeatcalendar.md) — The calendar the system should refer to when it reschedules a repeating notification. _(deprecated)_
- [region](region.md) — The geographic region that triggers the notification. _(deprecated)_
- [regionTriggersOnce](regiontriggersonce.md) — A Boolean value indicating whether crossing a geographic region boundary delivers only one notification. _(deprecated)_
