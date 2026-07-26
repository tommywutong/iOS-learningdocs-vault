---
title: timeZone
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilocalnotification/timezone
source_url: 'https://developer.apple.com/documentation/uikit/uilocalnotification/timezone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilocalnotification/timezone.json'
content_hash: 'sha256:66daffa5227b97a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILocalNotification](../uilocalnotification.md)

# timeZone

<sub>Instance Property</sub>

The time zone of the notification’s fire date.

> [!warning] Deprecated
> For more information, see [UILocalNotification](../uilocalnotification.md).

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
var timeZone: TimeZone? { get set }
```

## Discussion

The date specified in [fireDate](firedate.md) is interpreted according to the value of this property. If you specify `nil` (the default), the fire date is interpreted as an absolute GMT time, which is suitable for cases such as countdown timers. If you assign a valid [NSTimeZone](../../foundation/nstimezone.md) object to this property, the fire date is interpreted as a wall-clock time that is automatically adjusted when there are changes in time zones; an example suitable for this case is an an alarm clock.

## See Also

### Scheduling a local notification

- [fireDate](firedate.md) — The date and time when the system should deliver the notification. _(deprecated)_
- [repeatInterval](repeatinterval.md) — The calendar interval at which to reschedule the notification. _(deprecated)_
- [repeatCalendar](repeatcalendar.md) — The calendar the system should refer to when it reschedules a repeating notification. _(deprecated)_
- [region](region.md) — The geographic region that triggers the notification. _(deprecated)_
- [regionTriggersOnce](regiontriggersonce.md) — A Boolean value indicating whether crossing a geographic region boundary delivers only one notification. _(deprecated)_
