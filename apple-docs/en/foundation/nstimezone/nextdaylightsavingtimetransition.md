---
title: nextDaylightSavingTimeTransition
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstimezone/nextdaylightsavingtimetransition
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/nextdaylightsavingtimetransition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/nextdaylightsavingtimetransition.json'
content_hash: 'sha256:ba3bd1ede30da3c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# nextDaylightSavingTimeTransition

<sub>Instance Property</sub>

The date of the next daylight saving time transition for the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nextDaylightSavingTimeTransition: Date? { get }
```

## Discussion

This property contains the date of the next (after the current instant) daylight saving time transition for the receiver. Depending on the time zone of the receiver, the value of this property may represent a change of the time zone’s offset from GMT. Returns `nil` if the time zone of the receiver does not currently observe daylight saving time.

## See Also

### Working with Daylight Savings

- [daylightSavingTime](isdaylightsavingtime.md) — A Boolean value that indicates whether the receiver is currently using daylight saving time.
- [- isDaylightSavingTimeForDate:](<isdaylightsavingtime(for_).md>) — Indicates whether the receiver uses daylight saving time on a given date.
- [daylightSavingTimeOffset](daylightsavingtimeoffset.md) — The current daylight saving time offset of the receiver.
- [- daylightSavingTimeOffsetForDate:](<daylightsavingtimeoffset(for_).md>) — Returns the daylight saving time offset for a given date.
- [- nextDaylightSavingTimeTransitionAfterDate:](<nextdaylightsavingtimetransition(after_).md>) — Returns the next daylight saving time transition after a given date.
