---
title: region
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilocalnotification/region
source_url: 'https://developer.apple.com/documentation/uikit/uilocalnotification/region'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilocalnotification/region.json'
content_hash: 'sha256:8a9e9e16e694b457'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILocalNotification](../uilocalnotification.md)

# region

<sub>Instance Property</sub>

The geographic region that triggers the notification.

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
@NSCopying var region: CLRegion? { get set }
```

## Discussion

Assigning a value to this property causes the local notification to be delivered when the user crosses the region’s boundary. The region object itself defines whether the notification is triggered when the user enters or exits the region. The default value of this property is `nil`.

You may specify a value for this property or the [fireDate](firedate.md) property but not both. Attempting to schedule a local notification that contains both a region and fire date raises an exception.

Apps are limited in the total number of regions they may monitor at any given time, and local notifications configured with a region value count against that total. In addition, the user must grant permission for your app to use location-related information for the delivery of region-based local notifications to work. If the user denies your app’s request to use location services, local notifications configured with a region will not be delivered.

## See Also

### Scheduling a local notification

- [fireDate](firedate.md) — The date and time when the system should deliver the notification. _(deprecated)_
- [timeZone](timezone.md) — The time zone of the notification’s fire date. _(deprecated)_
- [repeatInterval](repeatinterval.md) — The calendar interval at which to reschedule the notification. _(deprecated)_
- [repeatCalendar](repeatcalendar.md) — The calendar the system should refer to when it reschedules a repeating notification. _(deprecated)_
- [regionTriggersOnce](regiontriggersonce.md) — A Boolean value indicating whether crossing a geographic region boundary delivers only one notification. _(deprecated)_
