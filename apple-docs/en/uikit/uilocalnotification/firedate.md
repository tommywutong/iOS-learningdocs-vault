---
title: fireDate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilocalnotification/firedate
source_url: 'https://developer.apple.com/documentation/uikit/uilocalnotification/firedate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilocalnotification/firedate.json'
content_hash: 'sha256:f77310923ab702e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILocalNotification](../uilocalnotification.md)

# fireDate

<sub>Instance Property</sub>

The date and time when the system should deliver the notification.

> [!warning] Deprecated
> For more information, see [UILocalNotification](../uilocalnotification.md).

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
var fireDate: Date? { get set }
```

## Discussion

The fire date is interpreted according to the value specified in the [timeZone](timezone.md) property. If the specified value is `nil` or is a date in the past, the notification is delivered immediately.

You may specify a value for this property or the [region](region.md) property but not both. Attempting to schedule a local notification that contains both a region and fire date raises an exception.

## See Also

### Scheduling a local notification

- [timeZone](timezone.md) — The time zone of the notification’s fire date. _(deprecated)_
- [repeatInterval](repeatinterval.md) — The calendar interval at which to reschedule the notification. _(deprecated)_
- [repeatCalendar](repeatcalendar.md) — The calendar the system should refer to when it reschedules a repeating notification. _(deprecated)_
- [region](region.md) — The geographic region that triggers the notification. _(deprecated)_
- [regionTriggersOnce](regiontriggersonce.md) — A Boolean value indicating whether crossing a geographic region boundary delivers only one notification. _(deprecated)_
