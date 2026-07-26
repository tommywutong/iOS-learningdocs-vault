---
title: timeZone
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/components/timezone
source_url: 'https://developer.apple.com/documentation/foundation/locale/components/timezone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/components/timezone.json'
content_hash: 'sha256:026ba182e47dd270'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Components](../components.md)

# timeZone

<sub>Instance Property</sub>

The time zone used by the locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var timeZone: TimeZone?
```

## Discussion

Set this value to specify a time zone associated with the locale.

This property corresponds to the `tz` key of the Unicode BCP 47 extension.

## See Also

### Specifying date and time components

- [calendar](calendar.md) — The calendar used by the locale.
- [Identifier](../../calendar/identifier-swift.enum.md) — An enumeration for the available calendars.
- [firstDayOfWeek](firstdayofweek.md) — The first day of the week as represented by this locale.
- [Weekday](../weekday.md) — A type that represents weekdays, used for indicating a locale’s first day of the week.
- [hourCycle](hourcycle.md) — The hour cycle used by the locale, like one-to-twelve or zero-to-twenty-three.
- [HourCycle](../hourcycle-swift.enum.md) — A type that represents the hour cycle used in a locale, like one-to-twelve or zero-to-twenty-three.
