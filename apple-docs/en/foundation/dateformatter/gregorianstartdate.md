---
title: gregorianStartDate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dateformatter/gregorianstartdate
source_url: 'https://developer.apple.com/documentation/foundation/dateformatter/gregorianstartdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateformatter/gregorianstartdate.json'
content_hash: 'sha256:abe8ba21e4ae2306'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateFormatter](../dateformatter.md)

# gregorianStartDate

<sub>Instance Property</sub>

The start date of the Gregorian calendar for the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var gregorianStartDate: Date? { get set }
```

## Discussion

This is used to specify the start date for the Gregorian calendar switch from the Julian calendar. Different locales switched at different times. Normally you should just accept the locale’s default date for the switch.

See [NSCalendar](../nscalendar.md) for more information.

## See Also

### Managing Attributes

- [calendar](calendar.md) — The calendar for the receiver.
- [defaultDate](defaultdate.md) — The default date for the receiver.
- [locale](locale.md) — The locale for the receiver.
- [timeZone](timezone.md) — The time zone for the receiver.
- [twoDigitStartDate](twodigitstartdate.md) — The earliest date that can be denoted by a two-digit year specifier.
