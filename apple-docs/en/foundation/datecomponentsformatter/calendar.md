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
doc_path: /documentation/foundation/datecomponentsformatter/calendar
source_url: 'https://developer.apple.com/documentation/foundation/datecomponentsformatter/calendar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponentsformatter/calendar.json'
content_hash: 'sha256:4df4593259d99b27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponentsFormatter](../datecomponentsformatter.md)

# calendar

<sub>Instance Property</sub>

The default calendar to use when formatting date components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var calendar: Calendar? { get set }
```

## Discussion

The formatter uses the calendar in this property to format values that do not have an inherent calendar of their own. For example, the formatter uses this calendar when formatting an [TimeInterval](../timeinterval.md) value.

The default value of this property is the calendar returned by the [autoupdatingCurrentCalendar](../nscalendar/autoupdatingcurrent.md) method of [NSCalendar](../nscalendar.md). Setting this property to `nil` causes the formatter to use the Gregorian calendar with the `en_US_POSIX` locale.

## See Also

### Configuring the Formatter Options

- [allowedUnits](allowedunits.md) — The bitmask of calendrical units such as day and month to include in the output string.
- [allowsFractionalUnits](allowsfractionalunits.md) — A Boolean indicating whether non-integer units may be used for values.
- [collapsesLargestUnit](collapseslargestunit.md) — A Boolean value indicating whether to collapse the largest unit into smaller units when a certain threshold is met.
- [includesApproximationPhrase](includesapproximationphrase.md) — A Boolean value indicating whether the resulting phrase reflects an inexact time value.
- [includesTimeRemainingPhrase](includestimeremainingphrase.md) — A Boolean value indicating whether output strings reflect the amount of time remaining.
- [maximumUnitCount](maximumunitcount.md) — The maximum number of time units to include in the output string.
- [unitsStyle](unitsstyle-swift.property.md) — The formatting style for unit names.
- [zeroFormattingBehavior](zeroformattingbehavior-swift.property.md) — The formatting style for units whose value is 0.
