---
title: timeZone
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dateformatter/timezone
source_url: 'https://developer.apple.com/documentation/foundation/dateformatter/timezone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateformatter/timezone.json'
content_hash: 'sha256:6faddc0c16973078'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateFormatter](../dateformatter.md)

# timeZone

<sub>Instance Property</sub>

The time zone for the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var timeZone: TimeZone! { get set }
```

## Discussion

If unspecified, the system time zone is used.

## See Also

### Managing Attributes

- [calendar](calendar.md) — The calendar for the receiver.
- [defaultDate](defaultdate.md) — The default date for the receiver.
- [locale](locale.md) — The locale for the receiver.
- [twoDigitStartDate](twodigitstartdate.md) — The earliest date that can be denoted by a two-digit year specifier.
- [gregorianStartDate](gregorianstartdate.md) — The start date of the Gregorian calendar for the receiver.
