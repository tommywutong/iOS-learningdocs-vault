---
title: twoDigitStartDate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dateformatter/twodigitstartdate
source_url: 'https://developer.apple.com/documentation/foundation/dateformatter/twodigitstartdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateformatter/twodigitstartdate.json'
content_hash: 'sha256:96555ea51500699f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateFormatter](../dateformatter.md)

# twoDigitStartDate

<sub>Instance Property</sub>

The earliest date that can be denoted by a two-digit year specifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var twoDigitStartDate: Date? { get set }
```

## Discussion

If the two-digit start date is set to January 6, 1976, then “January 1, 76” is interpreted as New Year’s Day in 2076, whereas “February 14, 76” is interpreted as Valentine’s Day in 1976.

By default, this property is equal to December 31, 1949.

## See Also

### Managing Attributes

- [calendar](calendar.md) — The calendar for the receiver.
- [defaultDate](defaultdate.md) — The default date for the receiver.
- [locale](locale.md) — The locale for the receiver.
- [timeZone](timezone.md) — The time zone for the receiver.
- [gregorianStartDate](gregorianstartdate.md) — The start date of the Gregorian calendar for the receiver.
