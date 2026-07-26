---
title: calendar
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/components/calendar
source_url: 'https://developer.apple.com/documentation/foundation/locale/components/calendar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/components/calendar.json'
content_hash: 'sha256:a9b719d866f9f899'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Components](../components.md)

# calendar

<sub>Instance Property</sub>

The calendar used by the locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var calendar: Calendar.Identifier?
```

## Discussion

Set this property to override the locale’s default calendar. To request the default calendar used by the locale, use the [Locale](../../locale.md) property [calendar](../calendar.md).

This property corresponds to the `ca` key of the Unicode BCP 47 extension.

## See Also

### Specifying date and time components

- [Identifier](../../calendar/identifier-swift.enum.md) — An enumeration for the available calendars.
- [firstDayOfWeek](firstdayofweek.md) — The first day of the week as represented by this locale.
- [Weekday](../weekday.md) — A type that represents weekdays, used for indicating a locale’s first day of the week.
- [hourCycle](hourcycle.md) — The hour cycle used by the locale, like one-to-twelve or zero-to-twenty-three.
- [HourCycle](../hourcycle-swift.enum.md) — A type that represents the hour cycle used in a locale, like one-to-twelve or zero-to-twenty-three.
- [timeZone](timezone.md) — The time zone used by the locale.
