---
title: current
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscalendar/current
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/current'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/current.json'
content_hash: 'sha256:60f348b24f01590f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# current

<sub>Type Property</sub>

The user’s current calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var current: Calendar { get }
```

## Return Value

The logical calendar for the current user.

## Discussion

The returned calendar is formed from the settings for the current user’s chosen system locale overlaid with any custom settings the user has specified in System Preferences. Settings you get from this calendar do not change as System Preferences are changed, so that your operations are consistent  (contrast with [autoupdatingCurrentCalendar](autoupdatingcurrent.md)).

## See Also

### Related Documentation

- [Date and Time Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i)
- [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i)
- [- initWithCalendarIdentifier:](<init(calendaridentifier_).md>) — Initializes a calendar according to a given identifier.
- [calendarIdentifier](calendaridentifier.md) — An identifier for the calendar.

### Getting the User’s Calendar

- [autoupdatingCurrentCalendar](autoupdatingcurrent.md) — A calendar that tracks changes to user’s preferred calendar.
