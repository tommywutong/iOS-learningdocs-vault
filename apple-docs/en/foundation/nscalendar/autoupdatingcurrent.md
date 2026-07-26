---
title: autoupdatingCurrent
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscalendar/autoupdatingcurrent
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/autoupdatingcurrent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/autoupdatingcurrent.json'
content_hash: 'sha256:504f4b47a59f9dff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# autoupdatingCurrent

<sub>Type Property</sub>

A calendar that tracks changes to user’s preferred calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var autoupdatingCurrent: Calendar { get }
```

## Return Value

The current logical calendar for the current user.

## Discussion

Settings you get from this calendar do change as the user’s settings change (contrast with [currentCalendar](current.md)).

Note that if you cache values based on the calendar or related information those caches will of course not be automatically updated by the updating of the calendar object.

## See Also

### Related Documentation

- [- initWithCalendarIdentifier:](<init(calendaridentifier_).md>) — Initializes a calendar according to a given identifier.
- [calendarIdentifier](calendaridentifier.md) — An identifier for the calendar.

### Getting the User’s Calendar

- [currentCalendar](current.md) — The user’s current calendar.
