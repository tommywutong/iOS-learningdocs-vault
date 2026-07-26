---
title: hourCycle
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/components/hourcycle
source_url: 'https://developer.apple.com/documentation/foundation/locale/components/hourcycle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/components/hourcycle.json'
content_hash: 'sha256:9cb0b98e93696e05'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Components](../components.md)

# hourCycle

<sub>Instance Property</sub>

The hour cycle used by the locale, like one-to-twelve or zero-to-twenty-three.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hourCycle: Locale.HourCycle?
```

## Discussion

Set this property to override the locale’s default hour cycle. To request the default hour cycle used by the locale, use the [Locale](../../locale.md) property `hourCycle`.

This property corresponds to the `hc` key of the Unicode BCP 47 extension.

## See Also

### Specifying date and time components

- [calendar](calendar.md) — The calendar used by the locale.
- [Identifier](../../calendar/identifier-swift.enum.md) — An enumeration for the available calendars.
- [firstDayOfWeek](firstdayofweek.md) — The first day of the week as represented by this locale.
- [Weekday](../weekday.md) — A type that represents weekdays, used for indicating a locale’s first day of the week.
- [HourCycle](../hourcycle-swift.enum.md) — A type that represents the hour cycle used in a locale, like one-to-twelve or zero-to-twenty-three.
- [timeZone](timezone.md) — The time zone used by the locale.
