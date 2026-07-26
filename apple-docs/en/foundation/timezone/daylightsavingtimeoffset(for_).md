---
title: 'daylightSavingTimeOffset(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/timezone/daylightsavingtimeoffset(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/timezone/daylightsavingtimeoffset(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timezone/daylightsavingtimeoffset%28for%3A%29.json'
content_hash: 'sha256:cd94699a6bafc6a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [TimeZone](../timezone.md)

# daylightSavingTimeOffset(for:)

<sub>Instance Method</sub>

Returns the daylight saving time offset for a given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func daylightSavingTimeOffset(for date: Date = Date()) -> TimeInterval
```

## Parameters

- `date` — The date to use for the calculation. The default value is the current date.

## See Also

### Working with Daylight Savings

- [isDaylightSavingTime(for:)](<isdaylightsavingtime(for_).md>) — Returns a Boolean value that indicates whether the receiver uses daylight saving time at a given date.
- [nextDaylightSavingTimeTransition](nextdaylightsavingtimetransition.md) — The date of the next (after the current instant) daylight saving time transition for the time zone.
- [nextDaylightSavingTimeTransition(after:)](<nextdaylightsavingtimetransition(after_).md>) — Returns the next daylight saving time transition after a given date.
