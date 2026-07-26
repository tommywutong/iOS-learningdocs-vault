---
title: 'daylightSavingTimeOffset(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstimezone/daylightsavingtimeoffset(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/daylightsavingtimeoffset(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/daylightsavingtimeoffset%28for%3A%29.json'
content_hash: 'sha256:c2fe86c9e83a4537'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# daylightSavingTimeOffset(for:)

<sub>Instance Method</sub>

Returns the daylight saving time offset for a given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func daylightSavingTimeOffset(for aDate: Date) -> TimeInterval
```

## Parameters

- `aDate` — A date.

## Return Value

The daylight saving time offset for `aDate`.

## See Also

### Working with Daylight Savings

- [daylightSavingTime](isdaylightsavingtime.md) — A Boolean value that indicates whether the receiver is currently using daylight saving time.
- [- isDaylightSavingTimeForDate:](<isdaylightsavingtime(for_).md>) — Indicates whether the receiver uses daylight saving time on a given date.
- [daylightSavingTimeOffset](daylightsavingtimeoffset.md) — The current daylight saving time offset of the receiver.
- [nextDaylightSavingTimeTransition](nextdaylightsavingtimetransition.md) — The date of the next daylight saving time transition for the receiver.
- [- nextDaylightSavingTimeTransitionAfterDate:](<nextdaylightsavingtimetransition(after_).md>) — Returns the next daylight saving time transition after a given date.
