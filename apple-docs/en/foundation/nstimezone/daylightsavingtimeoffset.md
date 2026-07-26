---
title: daylightSavingTimeOffset
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstimezone/daylightsavingtimeoffset
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/daylightsavingtimeoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/daylightsavingtimeoffset.json'
content_hash: 'sha256:6cb7c16397282865'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# daylightSavingTimeOffset

<sub>Instance Property</sub>

The current daylight saving time offset of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var daylightSavingTimeOffset: TimeInterval { get }
```

## See Also

### Working with Daylight Savings

- [daylightSavingTime](isdaylightsavingtime.md) — A Boolean value that indicates whether the receiver is currently using daylight saving time.
- [- isDaylightSavingTimeForDate:](<isdaylightsavingtime(for_).md>) — Indicates whether the receiver uses daylight saving time on a given date.
- [- daylightSavingTimeOffsetForDate:](<daylightsavingtimeoffset(for_).md>) — Returns the daylight saving time offset for a given date.
- [nextDaylightSavingTimeTransition](nextdaylightsavingtimetransition.md) — The date of the next daylight saving time transition for the receiver.
- [- nextDaylightSavingTimeTransitionAfterDate:](<nextdaylightsavingtimetransition(after_).md>) — Returns the next daylight saving time transition after a given date.
