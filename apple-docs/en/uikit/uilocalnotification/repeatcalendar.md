---
title: repeatCalendar
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilocalnotification/repeatcalendar
source_url: 'https://developer.apple.com/documentation/uikit/uilocalnotification/repeatcalendar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilocalnotification/repeatcalendar.json'
content_hash: 'sha256:717d5f36af1f793c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILocalNotification](../uilocalnotification.md)

# repeatCalendar

<sub>Instance Property</sub>

The calendar the system should refer to when it reschedules a repeating notification.

> [!warning] Deprecated
> For more information, see [UILocalNotification](../uilocalnotification.md).

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
var repeatCalendar: Calendar? { get set }
```

## Discussion

The default value is `nil`, which indicates that the current user calendar is used. (The current user calendar is returned by the [current](../../foundation/nscalendar/current.md) class method of `NSCalendar`.)

## See Also

### Scheduling a local notification

- [fireDate](firedate.md) — The date and time when the system should deliver the notification. _(deprecated)_
- [timeZone](timezone.md) — The time zone of the notification’s fire date. _(deprecated)_
- [repeatInterval](repeatinterval.md) — The calendar interval at which to reschedule the notification. _(deprecated)_
- [region](region.md) — The geographic region that triggers the notification. _(deprecated)_
- [regionTriggersOnce](regiontriggersonce.md) — A Boolean value indicating whether crossing a geographic region boundary delivers only one notification. _(deprecated)_
