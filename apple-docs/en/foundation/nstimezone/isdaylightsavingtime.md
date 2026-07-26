---
title: isDaylightSavingTime
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstimezone/isdaylightsavingtime
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/isdaylightsavingtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/isdaylightsavingtime.json'
content_hash: 'sha256:7b3fcdb288cc989d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# isDaylightSavingTime

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver is currently using daylight saving time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isDaylightSavingTime: Bool { get }
```

## Discussion

If [true](../../swift/true.md), the receiver is currently using daylight saving time, otherwise [false](../../swift/false.md). This property invokes [- isDaylightSavingTimeForDate:](<isdaylightsavingtime(for_).md>) with the current date as the argument.

## See Also

### Working with Daylight Savings

- [- isDaylightSavingTimeForDate:](<isdaylightsavingtime(for_).md>) — Indicates whether the receiver uses daylight saving time on a given date.
- [daylightSavingTimeOffset](daylightsavingtimeoffset.md) — The current daylight saving time offset of the receiver.
- [- daylightSavingTimeOffsetForDate:](<daylightsavingtimeoffset(for_).md>) — Returns the daylight saving time offset for a given date.
- [nextDaylightSavingTimeTransition](nextdaylightsavingtimetransition.md) — The date of the next daylight saving time transition for the receiver.
- [- nextDaylightSavingTimeTransitionAfterDate:](<nextdaylightsavingtimetransition(after_).md>) — Returns the next daylight saving time transition after a given date.
