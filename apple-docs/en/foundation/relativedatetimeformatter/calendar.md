---
title: calendar
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/relativedatetimeformatter/calendar
source_url: 'https://developer.apple.com/documentation/foundation/relativedatetimeformatter/calendar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/relativedatetimeformatter/calendar.json'
content_hash: 'sha256:d5138a07a24eb507'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RelativeDateTimeFormatter](../relativedatetimeformatter.md)

# calendar

<sub>Instance Property</sub>

The calendar to use for formatting values that don’t have an inherent calendar of their own.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var calendar: Calendar! { get set }
```

## Discussion

Defaults to [autoupdatingCurrentCalendar](../nscalendar/autoupdatingcurrent.md). If you set this property to `nil`, the formatter resets to using [autoupdatingCurrentCalendar](../nscalendar/autoupdatingcurrent.md).

## See Also

### Configuring Formatter Options

- [locale](locale.md) — The locale to use when formatting the date.
- [dateTimeStyle](datetimestyle-swift.property.md) — The style to use when describing a relative date, for example “yesterday” or “1 day ago”.
- [DateTimeStyle](datetimestyle-swift.enum.md) — A type that represents the style to use when formatting relative dates, such as “1 week ago” or “last week”.
- [unitsStyle](unitsstyle-swift.property.md) — The style to use when formatting the quantity or the name of the unit, such as “1 day ago” or “one day ago”.
- [UnitsStyle](unitsstyle-swift.enum.md) — A type that represents the style to use when formatting the units of relative dates.
- [formattingContext](formattingcontext.md) — A description of where the formatted string will appear, allowing the formatter to capitalize the output appropriately.
