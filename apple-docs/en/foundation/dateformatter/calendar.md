---
title: calendar
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dateformatter/calendar
source_url: 'https://developer.apple.com/documentation/foundation/dateformatter/calendar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateformatter/calendar.json'
content_hash: 'sha256:f3433dfa3ae6bddc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateFormatter](../dateformatter.md)

# calendar

<sub>Instance Property</sub>

The calendar for the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var calendar: Calendar! { get set }
```

## Discussion

If unspecified, the logical calendar for the current user is used.

## See Also

### Managing Attributes

- [defaultDate](defaultdate.md) — The default date for the receiver.
- [locale](locale.md) — The locale for the receiver.
- [timeZone](timezone.md) — The time zone for the receiver.
- [twoDigitStartDate](twodigitstartdate.md) — The earliest date that can be denoted by a two-digit year specifier.
- [gregorianStartDate](gregorianstartdate.md) — The start date of the Gregorian calendar for the receiver.
