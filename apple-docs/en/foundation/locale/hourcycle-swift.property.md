---
title: hourCycle
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/hourcycle-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/locale/hourcycle-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/hourcycle-swift.property.json'
content_hash: 'sha256:ab2c8c7760fc0d58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# hourCycle

<sub>Instance Property</sub>

The hour cycle used by the locale, like one-to-twelve or zero-to-twenty-three.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hourCycle: Locale.HourCycle { get }
```

## Discussion

When called on the special [Locale](../locale.md) instances [current](current.md) or [autoupdatingCurrent](autoupdatingcurrent.md), if the user overrode the default hour cycle, this property provides the user’s preference.

This property corresponds to the `hc` key of the Unicode BCP 47 extension.

For locale instances created with the `hc` specifier (such as `en-US@hc=h23`), or with a custom [Components](components.md), this property represents the custom hour cycle. Otherwise, it represents the locale’s default hour cycle.

## See Also

### Getting date and time components

- [firstDayOfWeek](firstdayofweek.md) — The first day of the week as represented by this locale.
- [Weekday](weekday.md) — A type that represents weekdays, used for indicating a locale’s first day of the week.
- [HourCycle](hourcycle-swift.enum.md) — A type that represents the hour cycle used in a locale, like one-to-twelve or zero-to-twenty-three.
- [timeZone](timezone.md) — The time zone associated with the locale, if any.
