---
title: 'isDaylightSavingTime(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstimezone/isdaylightsavingtime(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/isdaylightsavingtime(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/isdaylightsavingtime%28for%3A%29.json'
content_hash: 'sha256:0098287e3e33d99b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# isDaylightSavingTime(for:)

<sub>Instance Method</sub>

Indicates whether the receiver uses daylight saving time on a given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isDaylightSavingTime(for aDate: Date) -> Bool
```

## Parameters

- `aDate` — The date against which to test the receiver.

## Return Value

[true](../../swift/true.md) if the receiver uses daylight saving time at `aDate`, otherwise [false](../../swift/false.md).

## See Also

### Working with Daylight Savings

- [daylightSavingTime](isdaylightsavingtime.md) — A Boolean value that indicates whether the receiver is currently using daylight saving time.
- [daylightSavingTimeOffset](daylightsavingtimeoffset.md) — The current daylight saving time offset of the receiver.
- [- daylightSavingTimeOffsetForDate:](<daylightsavingtimeoffset(for_).md>) — Returns the daylight saving time offset for a given date.
- [nextDaylightSavingTimeTransition](nextdaylightsavingtimetransition.md) — The date of the next daylight saving time transition for the receiver.
- [- nextDaylightSavingTimeTransitionAfterDate:](<nextdaylightsavingtimetransition(after_).md>) — Returns the next daylight saving time transition after a given date.
