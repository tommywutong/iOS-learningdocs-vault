---
title: calendar
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/relativeformatstyle/calendar
source_url: 'https://developer.apple.com/documentation/foundation/date/relativeformatstyle/calendar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/relativeformatstyle/calendar.json'
content_hash: 'sha256:a6e92ae04447d348'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [RelativeFormatStyle](../relativeformatstyle.md)

# calendar

<sub>Instance Property</sub>

The calendar to use when formatting relative dates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var calendar: Calendar
```

## Discussion

Defaults to [autoupdatingCurrentCalendar](../../nscalendar/autoupdatingcurrent.md). If you set this property to `nil`, the format style resets to using [autoupdatingCurrentCalendar](../../nscalendar/autoupdatingcurrent.md).

## See Also

### Modifying a Relative Date Format Style

- [presentation](presentation-swift.property.md) — Specifies the style to use when describing a relative date, such as “1 day ago” or “yesterday”.
- [unitsStyle](unitsstyle-swift.property.md) — The style to use when formatting the quantity or the name of the unit, such as “1 day ago” or “one day ago”.
- [capitalizationContext](capitalizationcontext.md) — The capitalization context to use when formatting the relative dates.
- [locale](locale.md) — The locale to use when formatting the relative date.
- [locale(_:)](<locale(__).md>) — Modifies the relative date format style to use the specified locale.
