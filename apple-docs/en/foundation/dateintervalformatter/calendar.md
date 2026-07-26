---
title: calendar
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dateintervalformatter/calendar
source_url: 'https://developer.apple.com/documentation/foundation/dateintervalformatter/calendar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateintervalformatter/calendar.json'
content_hash: 'sha256:15aaa60868882bfb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateIntervalFormatter](../dateintervalformatter.md)

# calendar

<sub>Instance Property</sub>

The calendar to use for date values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var calendar: Calendar! { get set }
```

## Discussion

The default value of this property is the calendar associated with the current [locale](locale.md) object. You can change this value to use a different calendar for interpreting dates.

## See Also

### Configuring the Formatter Options

- [dateStyle](datestyle.md) — The style to use when formatting day, month, and year information.
- [timeStyle](timestyle.md) — The style to use when formatting hour, minute, and second information.
- [dateTemplate](datetemplate.md) — The template for formatting one date and time value.
- [locale](locale.md) — The locale to use when formatting date and time values.
- [timeZone](timezone.md) — The time zone with which to specify time values.
