---
title: locale
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/locale
source_url: 'https://developer.apple.com/documentation/foundation/calendar/locale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/locale.json'
content_hash: 'sha256:67929f35c6390c22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# locale

<sub>Instance Property</sub>

The locale of the calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var locale: Locale? { get set }
```

## See Also

### Getting Calendar Information

- [identifier](identifier-swift.property.md) — The identifier of the calendar.
- [firstWeekday](firstweekday.md) — The first day of the week for the calendar.
- [minimumDaysInFirstWeek](minimumdaysinfirstweek.md) — The number of minimum days in the first week.
- [timeZone](timezone.md) — The time zone of the calendar.
- [maximumRange(of:)](<maximumrange(of_).md>) — The maximum range limits of the values that a given component can take on.
- [minimumRange(of:)](<minimumrange(of_).md>) — Returns the minimum range limits of the values that a given component can take on.
- [ordinality(of:in:for:)](<ordinality(of_in_for_).md>) — Returns, for a given absolute time, the ordinal number of a smaller calendar component (such as a day) within a specified larger calendar component (such as a week).
- [range(of:in:for:)](<range(of_in_for_).md>) — Returns the range of absolute time values that a smaller calendar component (such as a day) can take on in a larger calendar component (such as a month) that includes a specified absolute time.
