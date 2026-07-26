---
title: firstDayOfWeek
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/components/firstdayofweek
source_url: 'https://developer.apple.com/documentation/foundation/locale/components/firstdayofweek'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/components/firstdayofweek.json'
content_hash: 'sha256:fe08b4e9d2416307'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Components](../components.md)

# firstDayOfWeek

<sub>Instance Property</sub>

The first day of the week as represented by this locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var firstDayOfWeek: Locale.Weekday?
```

## Discussion

This value is the preferred first day of the week to show in a calendar view. It isn’t necessarily the same as the first day after the weekend; don’t try to determine a first-day-of-week value from weekend information.

Set this property to override the locale’s default first day of week. To request the default first day of week used by the locale, use the [Locale](../../locale.md) property `firstDayOfWeek`.

This property corresponds to the `fw` key of the Unicode BCP 47 extension.

## See Also

### Specifying date and time components

- [calendar](calendar.md) — The calendar used by the locale.
- [Identifier](../../calendar/identifier-swift.enum.md) — An enumeration for the available calendars.
- [Weekday](../weekday.md) — A type that represents weekdays, used for indicating a locale’s first day of the week.
- [hourCycle](hourcycle.md) — The hour cycle used by the locale, like one-to-twelve or zero-to-twenty-three.
- [HourCycle](../hourcycle-swift.enum.md) — A type that represents the hour cycle used in a locale, like one-to-twelve or zero-to-twenty-three.
- [timeZone](timezone.md) — The time zone used by the locale.
