---
title: firstWeekday
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/firstweekday
source_url: 'https://developer.apple.com/documentation/foundation/calendar/firstweekday'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/firstweekday.json'
content_hash: 'sha256:22470bd1003ce002'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# firstWeekday

<sub>Instance Property</sub>

The first day of the week for the calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var firstWeekday: Int { get set }
```

## Discussion

The default value of [firstWeekday](firstweekday.md) varies by calendar and locale. Your app can reset this value.

The weekday units are one-based. For Gregorian and ISO 8601 calendars, `1` is Sunday.

## See Also

### Getting Calendar Information

- [identifier](identifier-swift.property.md) — The identifier of the calendar.
- [locale](locale.md) — The locale of the calendar.
- [minimumDaysInFirstWeek](minimumdaysinfirstweek.md) — The number of minimum days in the first week.
- [timeZone](timezone.md) — The time zone of the calendar.
- [maximumRange(of:)](<maximumrange(of_).md>) — The maximum range limits of the values that a given component can take on.
- [minimumRange(of:)](<minimumrange(of_).md>) — Returns the minimum range limits of the values that a given component can take on.
- [ordinality(of:in:for:)](<ordinality(of_in_for_).md>) — Returns, for a given absolute time, the ordinal number of a smaller calendar component (such as a day) within a specified larger calendar component (such as a week).
- [range(of:in:for:)](<range(of_in_for_).md>) — Returns the range of absolute time values that a smaller calendar component (such as a day) can take on in a larger calendar component (such as a month) that includes a specified absolute time.
