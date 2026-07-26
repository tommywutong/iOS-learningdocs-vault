---
title: NSCalendarDayChanged
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nscalendardaychanged
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nscalendardaychanged'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nscalendardaychanged.json'
content_hash: 'sha256:d2cff7828c8bdffb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSCalendarDayChanged

<sub>Type Property</sub>

A notification that is posted whenever the calendar day of the system changes, as determined by the system calendar, locale, and time zone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let NSCalendarDayChanged: NSNotification.Name
```

## Discussion

If the the device is asleep when the day changes, this notification will be posted on wakeup. Only one notification will be posted on wakeup if the device has been asleep for multiple days.

There are no guarantees about the timeliness of when this notification will be received by observers. As such, you should not rely on this notification being posted or received at any precise time.
