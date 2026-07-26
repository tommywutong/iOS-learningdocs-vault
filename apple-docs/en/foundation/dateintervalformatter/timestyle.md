---
title: timeStyle
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dateintervalformatter/timestyle
source_url: 'https://developer.apple.com/documentation/foundation/dateintervalformatter/timestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateintervalformatter/timestyle.json'
content_hash: 'sha256:4048edd97d2d25d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateIntervalFormatter](../dateintervalformatter.md)

# timeStyle

<sub>Instance Property</sub>

The style to use when formatting hour, minute, and second information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var timeStyle: DateIntervalFormatter.Style { get set }
```

## Discussion

Set this property to an appropriate value before generating string values. The default value of this property is [NSDateIntervalFormatterNoStyle](style/none.md).

## See Also

### Configuring the Formatter Options

- [dateStyle](datestyle.md) — The style to use when formatting day, month, and year information.
- [dateTemplate](datetemplate.md) — The template for formatting one date and time value.
- [calendar](calendar.md) — The calendar to use for date values.
- [locale](locale.md) — The locale to use when formatting date and time values.
- [timeZone](timezone.md) — The time zone with which to specify time values.
